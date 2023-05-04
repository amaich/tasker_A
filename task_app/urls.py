from django.urls import path
from .views import *

app_name = 'task_app'

urlpatterns = [
    path('', hello_world),
    path('tasks/', TaskListView.as_view(), name='task_list'),
    path('tasks/create', TaskCreateView.as_view(), name='task_create'),
    path('tasks/<slug:slug>/', TaskDetailView.as_view(), name='task_detail'),
    path('tasks/<slug:slug>/', TaskUpdateView.as_view(), name='task_update'),
]
