from django.urls import path
from .views import *

app_name = "list"

urlpatterns = [
    path('', home, name="home"),
    path('<int:list_id>', list_view, name="list_view"),
    path('create-list', create_list, name="create_list"),
    path('delete-list/<int:list_id>', delete_list, name="delete_list"),
    path('delete-task/<int:task_id>', delete_task, name="delete_task"),
    path('check-task/<int:task_id>', change_task_status, name="check_task"),
    path('change-task-content/<int:task_id>/<str:content>', change_task_content, name="change-task-content"),
]