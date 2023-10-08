from django.urls import path
from .views import homePage, create, update, delete, mark_completed

urlpatterns = [
    path('', homePage, name='home'),
    path('create', create, name='create'),
    path('update/<int:task_id>', update, name='update'),
    path('delete/<int:task_id>', delete, name='delete'),
    path('completed/<int:task_id>', mark_completed, name='completed'),
]