from django.urls import path
from .views import view_tasks, add_task, get_task, edit_task

urlpatterns = [
    path('', view_tasks, name='view_tasks'),
    path('add/', add_task, name='add-task'),
    path('<int:id>/', get_task, name='get-task'),
    path('edit-task/<str:id>/', edit_task, name='edit_task'),
]
