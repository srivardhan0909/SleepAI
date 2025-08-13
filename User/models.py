from django.db import models

class SleepDisorderPrediction(models.Model):
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    occupation = models.CharField(max_length=50)
    sleep_duration = models.FloatField()
    quality_of_sleep = models.IntegerField()
    physical_activity = models.IntegerField()
    stress_level = models.IntegerField()
    bmi_category = models.CharField(max_length=20)
    blood_pressure = models.CharField(max_length=10)
    heart_rate = models.IntegerField()
    daily_steps = models.IntegerField()
    prediction_result = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.gender} - {self.age} - {self.prediction_result}"
