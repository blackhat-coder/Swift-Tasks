
from django.contrib import admin
from .views import home_view, view_todo, update, delete
from django.urls import path

urlpatterns = [
    path('', home_view, name='home_view'),
    path('<int:pk>/', view_todo, name='view_todo'),
    path('update/<int:pk>/', update, name='update'),
    path('delete/<int:pk>/', delete, name='delete'),
]