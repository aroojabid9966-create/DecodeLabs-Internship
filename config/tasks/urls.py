from django.urls import path
from .views import task_list_creat, task_detail
urlpatterns = [
    path('tasks/', task_list_creat, name='task-list-creat'),
    path('tasks/<int:pk>/', task_detail, name='task-detail'),
]