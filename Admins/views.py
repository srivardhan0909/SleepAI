from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Count
from User.models import SleepDisorderPrediction
from django.core.paginator import Paginator
import json

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np

def adminhome(request):
    users = User.objects.filter(is_staff=False, is_superuser=False) 
    return render(request, "Admin/adminhome.html", {"users": users})

def admin_update_userstatus(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        
        # Toggle the is_active status
        user.is_active = not user.is_active
        user.save()

        # Display message based on the action
        if user.is_active:
            messages.success(request, f"User {user.username} has been activated.")
        else:
            messages.success(request, f"User {user.username} has been deactivated.")
        
        return redirect('adminhome')  # Redirect back to the admin home page
    except User.DoesNotExist:
        messages.error(request, "User not found.")
        return redirect('adminhome')
    
def admingraphs(request):
    try:
        # Check if there are any predictions in the database
        total_predictions = SleepDisorderPrediction.objects.count()
        print(f"Total predictions in database: {total_predictions}")

        if total_predictions == 0:
            return render(request, 'Admin/admingraphs.html', {
                'error': 'No predictions found in the database. Please add some predictions first.'
            })

        # Data for gender distribution
        gender_data = list(SleepDisorderPrediction.objects.values('gender').annotate(count=Count('id')))
        gender_labels = [item['gender'] for item in gender_data]
        gender_counts = [item['count'] for item in gender_data]
        print(f"Gender data - Labels: {gender_labels}, Counts: {gender_counts}")

        # Data for BMI distribution
        bmi_data = list(SleepDisorderPrediction.objects.values('bmi_category').annotate(count=Count('id')))
        bmi_labels = [item['bmi_category'] for item in bmi_data]
        bmi_counts = [item['count'] for item in bmi_data]
        print(f"BMI data - Labels: {bmi_labels}, Counts: {bmi_counts}")

        # Data for blood pressure distribution
        bp_data = list(SleepDisorderPrediction.objects.values('blood_pressure').annotate(count=Count('id')))
        bp_labels = [item['blood_pressure'] for item in bp_data]
        bp_counts = [item['count'] for item in bp_data]
        print(f"Blood Pressure data - Labels: {bp_labels}, Counts: {bp_counts}")

        # Data for prediction results
        result_data = list(SleepDisorderPrediction.objects.values('prediction_result').annotate(count=Count('id')))
        result_labels = [item['prediction_result'] for item in result_data]
        result_counts = [item['count'] for item in result_data]
        print(f"Result data - Labels: {result_labels}, Counts: {result_counts}")

        # Ensure all data is properly formatted for JSON
        context = {
            'gender_labels': json.dumps(gender_labels),
            'gender_counts': json.dumps(gender_counts),
            'bmi_labels': json.dumps(bmi_labels),
            'bmi_counts': json.dumps(bmi_counts),
            'bp_labels': json.dumps(bp_labels),
            'bp_counts': json.dumps(bp_counts),
            'result_labels': json.dumps(result_labels),
            'result_counts': json.dumps(result_counts),
        }

        return render(request, 'Admin/admingraphs.html', context)
    except Exception as e:
        print(f"Error in admingraphs view: {str(e)}")
        return render(request, 'Admin/admingraphs.html', {'error': str(e)})

def adminaccuracy(request):
    if request.method == "POST" and request.FILES.get("dataset"):
        try:
            # Handle file upload
            dataset_file = request.FILES["dataset"]
            data = pd.read_csv(dataset_file)

            # Preprocessing
            data = data.drop(columns=["Person ID"])  # Adjust column names as needed
            X = data.drop(columns=["Sleep Disorder"])
            y = data["Sleep Disorder"]

            # Label encoding
            label_encoders = {}
            for col in X.select_dtypes(include=["object"]).columns:
                le = LabelEncoder()
                X[col] = le.fit_transform(X[col])
                label_encoders[col] = dict(zip(le.classes_, le.transform(le.classes_)))
            if y.dtype == "object":
                target_encoder = LabelEncoder()
                y = target_encoder.fit_transform(y)

            # Split data
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            # Initialize results
            results = []

            # KNN
            knn = KNeighborsClassifier()
            knn.fit(X_train, y_train)
            knn_accuracy = knn.score(X_test, y_test)
            results.append({"Model": "KNN", "Accuracy": knn_accuracy})

            # SVM
            svm = SVC(probability=True)
            svm.fit(X_train, y_train)
            svm_accuracy = svm.score(X_test, y_test)
            results.append({"Model": "SVM", "Accuracy": svm_accuracy})

            # Decision Tree
            dt = DecisionTreeClassifier()
            dt.fit(X_train, y_train)
            dt_accuracy = dt.score(X_test, y_test)
            results.append({"Model": "Decision Tree", "Accuracy": dt_accuracy})

            # Random Forest
            rf = RandomForestClassifier()
            rf.fit(X_train, y_train)
            rf_accuracy = rf.score(X_test, y_test)
            results.append({"Model": "Random Forest", "Accuracy": rf_accuracy})

            # ANN
            ann = Sequential([
                Dense(64, activation='relu', input_dim=X_train.shape[1]),
                Dense(32, activation='relu'),
                Dense(len(set(y)), activation='softmax')
            ])
            ann.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
            ann.fit(X_train, y_train, epochs=10, batch_size=16, verbose=0)
            ann_accuracy = ann.evaluate(X_test, y_test, verbose=0)[1]
            results.append({"Model": "ANN", "Accuracy": ann_accuracy})

            # Hybrid Model
            rf_proba_train = rf.predict_proba(X_train)
            rf_proba_test = rf.predict_proba(X_test)
            X_train_hybrid = np.hstack((X_train, rf_proba_train))
            X_test_hybrid = np.hstack((X_test, rf_proba_test))
            scaler = StandardScaler()
            X_train_hybrid = scaler.fit_transform(X_train_hybrid)
            X_test_hybrid = scaler.transform(X_test_hybrid)
            hybrid_ann = Sequential([
                Dense(128, activation='relu', input_dim=X_train_hybrid.shape[1]),
                Dense(64, activation='relu'),
                Dense(len(set(y)), activation='softmax')
            ])
            hybrid_ann.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
            hybrid_ann.fit(X_train_hybrid, y_train, epochs=30, batch_size=16, verbose=0)
            hybrid_accuracy = hybrid_ann.evaluate(X_test_hybrid, y_test, verbose=0)[1]
            results.append({"Model": "Hybrid (RF + ANN)", "Accuracy": hybrid_accuracy})

            # Prepare data for template
            models = [result["Model"] for result in results]
            accuracies = [result["Accuracy"] for result in results]

            return render(request, "Admin/adminaccuracy.html", {
                "results": results,
                "models": models,
                "accuracies": accuracies
            })

        except Exception as e:
            return render(request, "Admin/adminaccuracy.html", {"error": str(e)})

    return render(request, "Admin/adminaccuracy.html")

def admindisplaypredictions(request):
    predictions = SleepDisorderPrediction.objects.all().order_by('-created_at')
    
    # Paginate with 10 objects per page
    paginator = Paginator(predictions, 10)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'Admin/admindisplaypredictions.html', {'page_obj': page_obj})
