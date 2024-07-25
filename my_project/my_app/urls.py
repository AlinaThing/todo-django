from django.urls import path
from .views import Todolists, success, DeleteTodoItem,EditTodoItem

urlpatterns = [
    path('', Todolists, name='Todolists'),
    path('success/', success, name='success'),
    path('delete/<int:pk>/', DeleteTodoItem, name='delete_todo_item'),
    path('edit/<int:pk>/', EditTodoItem, name= 'edit_todo_item'),
]
