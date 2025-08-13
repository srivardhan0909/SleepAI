from django.urls import path
from . import views

urlpatterns = [
    path('userhome/', views.userhome, name='userhome'),
    path('user_predict_sleep_disorder/', views.user_predict_sleep_disorder, name='user_predict_sleep_disorder'),
]
