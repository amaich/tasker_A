from django.urls import path
from .views import *

app_name = 'task_auth'

urlpatterns = [
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', user_logout, name='logout'),
    path('registration/', UserRegistration.as_view(), name='registration'),
    path('check/', is_auth_check, name='auth_check'),



]
