from django.shortcuts import render
from .models import SleepDisorderPrediction
import joblib
import numpy as np
from hybrid_model import HybridModel

# Create your views here.
def userhome(request):
    user = request.user
    return render(request, 'User/userhome.html', {'user':user})

# Define the model path
hybrid_model_path = "model/rfann_hybrid_model.pkl"

# Load the model
hybrid_model = joblib.load(hybrid_model_path)

def user_predict_sleep_disorder(request):
    if request.method == "POST":
        try:
            # Collect user inputs
            gender = request.POST.get("gender", "").strip().title()
            age = int(request.POST.get("age", "").strip())
            occupation = request.POST.get("occupation", "").strip().title()
            sleep_duration = float(request.POST.get("sleep_duration", "").strip())
            quality_of_sleep = int(request.POST.get("quality_of_sleep", "").strip())
            physical_activity = int(request.POST.get("physical_activity", "").strip())
            stress_level = int(request.POST.get("stress_level", "").strip())
            bmi_category = request.POST.get("bmi_category", "").strip().title()
            blood_pressure = request.POST.get("blood_pressure", "").strip()
            heart_rate = int(request.POST.get("heart_rate", "").strip())
            daily_steps = int(request.POST.get("daily_steps", "").strip())

            # Define mappings
            gender_mapping = {'Female': 0, 'Male': 1}
            occupation_mapping = {
                'Accountant': 0, 'Doctor': 1, 'Engineer': 2, 'Lawyer': 3, 'Manager': 4,
                'Nurse': 5, 'Sales Representative': 6, 'Salesperson': 7, 'Scientist': 8,
                'Software Engineer': 9, 'Teacher': 10
            }
            bmi_mapping = {'Normal': 0, 'Normal Weight': 1, 'Obese': 2, 'Overweight': 3}
            blood_pressure_mapping = {
                '115/75': 0, '115/78': 1, '117/76': 2, '118/75': 3, '118/76': 4,
                '119/77': 5, '120/80': 6, '121/79': 7, '122/80': 8, '125/80': 9,
                '125/82': 10, '126/83': 11, '128/84': 12, '128/85': 13, '129/84': 14,
                '130/85': 15, '130/86': 16, '131/86': 17, '132/87': 18, '135/88': 19,
                '135/90': 20, '139/91': 21, '140/90': 22, '140/95': 23, '142/92': 24
            }
            target_mapping = {0: 'Insomnia', 1: 'Sleep Apnea', 2: 'No-disorder'}

            # Prepare input array
            input_data = [
                gender_mapping.get(gender, -1),
                age,
                occupation_mapping.get(occupation, -1),
                sleep_duration,
                quality_of_sleep,
                physical_activity,
                stress_level,
                bmi_mapping.get(bmi_category, -1),
                blood_pressure_mapping.get(blood_pressure, -1),
                heart_rate,
                daily_steps,
            ]

            # Validate input
            if -1 in input_data:
                return render(request, "User/userpredict.html", {
                    "error": "Some inputs could not be mapped correctly. Please check your inputs."
                })

            # Convert to NumPy array and predict
            input_array = np.array(input_data).reshape(1, -1)
            prediction = hybrid_model.predict(input_array)
            predicted_class = np.argmax(prediction)
            result = target_mapping.get(predicted_class, "Unknown")

            # Save inputs and results in the database
            SleepDisorderPrediction.objects.create(
                gender=gender,
                age=age,
                occupation=occupation,
                sleep_duration=sleep_duration,
                quality_of_sleep=quality_of_sleep,
                physical_activity=physical_activity,
                stress_level=stress_level,
                bmi_category=bmi_category,
                blood_pressure=blood_pressure,
                heart_rate=heart_rate,
                daily_steps=daily_steps,
                prediction_result=result
            )

            return render(request, "User/userpredict.html", {"result": result})

        except Exception as e:
            return render(request, "User/userpredict.html", {"error": str(e)})

    return render(request, "User/userpredict.html")
