from django.urls import path
from Admins.views import *

urlpatterns = [
    path('adminhome/', adminhome, name='adminhome'),
    path('admin_update_userstatus/<int:user_id>/', admin_update_userstatus, name='admin_update_userstatus'),
    path('admingraphs/', admingraphs, name='admingraphs'),
    path('adminaccuracy/', adminaccuracy, name='adminaccuracy'),
    path('admindisplaypredictions', admindisplaypredictions, name='admindisplaypredictions')
]