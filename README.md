# 💤 SleepAI - Sleep Disorder Classification System



> An intelligent web application that leverages machine learning to accurately classify and predict sleep disorders based on patient health data.

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.0+-darkgreen.svg)](https://www.djangoproject.com/)

## ✨ Features

- **🧠 Smart Classification** - Utilizes hybrid ML models to predict sleep disorders with high accuracy
- **🔐 Secure Authentication** - Role-based access control for users and administrators
- **📊 Interactive Dashboard** - Rich visualizations and analytics for comprehensive insights
- **👤 User-friendly Portal** - Intuitive interface for submitting health data and viewing results
- **📱 Responsive Design** - Seamless experience across all devices


## 🛠️ Tech Stack

<table>
  <tr>
    <td align="center"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg" width="40" height="40"/><br>HTML5</td>
    <td align="center"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg" width="40" height="40"/><br>CSS3</td>
    <td align="center"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" width="40" height="40"/><br>JavaScript</td>
    <td align="center"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/bootstrap/bootstrap-original.svg" width="40" height="40"/><br>Bootstrap</td>
    <td align="center"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="40" height="40"/><br>Python</td>
    <td align="center"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg" width="40" height="40"/><br>Django</td>
    <td align="center"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlite/sqlite-original.svg" width="40" height="40"/><br>SQLite</td>
  </tr>
</table>

## 🚀 Installation

### Prerequisites
- Python 3.9+
- pip (Python package manager)

### Step-by-step setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/sleepai.git
   cd sleepai
   ```

2. **Create and activate virtual environment (recommended)**
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations**
   ```bash
   python manage.py migrate
   ```

5. **Run the development server**
   ```bash
   python manage.py runserver
   ```

6. **Access the application**
   - Open your browser and go to `http://127.0.0.1:8000`

## 🔍 How It Works

### Sleep Disorder Classification Logic

Our application employs a sophisticated hybrid model that analyzes multiple health factors to classify sleep disorders:

#### 🫁 Sleep Apnea Indicators
- BMI in the obese category (≥30)
- High blood pressure (>130/85 mmHg)
- Sleep duration less than 6 hours
- Age greater than 35 years
- Low physical activity levels
- High stress levels

#### 😴 Insomnia Indicators
- Sleep duration less than 6 hours
- Poor sleep quality rating
- High stress levels
- Limited physical activity
- Heightened anxiety symptoms

#### ✅ No Sleep Disorder Indicators
- Normal BMI range (18.5-24.9)
- Normal blood pressure (<120/80 mmHg)
- Regular physical activity
- Good sleep quality rating
- Moderate to low stress levels

## 👤 User Journey

1. **Register/Login** - Create an account or sign in
2. **Complete Profile** - Enter personal and health information
3. **Submit Data** - Provide sleep-related metrics and symptoms
4. **View Prediction** - Receive AI-generated sleep disorder classification
5. **Review Recommendations** - Get personalized suggestions based on results

## 🔐 Admin Access

```
Username: admin
Password: adm1n@2025
```

The admin dashboard provides:
- User management capabilities
- ML model performance metrics
- Data visualization and analytics
- System configuration options

## 📊 Data Visualization

SleepAI provides rich visualization tools to help understand:
- Sleep disorder distribution across demographics
- Correlation between health factors and sleep disorders
- Prediction accuracy metrics
- User engagement and system usage statistics


## 📚 Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [scikit-learn Documentation](https://scikit-learn.org/stable/documentation.html)
- [Bootstrap Documentation](https://getbootstrap.com/docs/)
- [Chart.js Documentation](https://www.chartjs.org/docs/latest/)

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- [Django Framework](https://www.djangoproject.com/) - The web framework used
- [scikit-learn](https://scikit-learn.org/) - Machine learning library
- [Bootstrap](https://getbootstrap.com/) - Frontend component library
- [Chart.js](https://www.chartjs.org/) - Data visualization library

---

<div align="center">
  <p>
    <a href="https://github.com/yourusername"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/></a>
    <a href="https://linkedin.com/in/yourusername"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
  </p>
</div>
