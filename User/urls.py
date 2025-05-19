from django.urls import path
from User.views import *

urlpatterns = [
    path('userhome/', userhome, name='userhome'),
   path('user_predict_sleep_disorder/', user_predict_sleep_disorder, name='user_predict_sleep_disorder'),

]