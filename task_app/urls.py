from django.urls import path
from .views import *

app_name = 'task_app'

urlpatterns = [
    path('', start_page, name='start_page'),
    path('tasks/', TaskListView.as_view(), name='task_list'),
    path('tasks/create', TaskCreateView.as_view(), name='task_create'),
    path('tasks/<int:pk>', TaskDetailView.as_view(), name='task_detail'),
    path('tasks/<int:pk>/update', TaskUpdateView.as_view(), name='task_update'),
    path('tasks/<int:pk>/delete', TaskDeleteView.as_view(), name='task_delete'),
]
