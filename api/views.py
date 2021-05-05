from django.shortcuts import render
from rest_framework import generics
from tapp.models import TodoModel
from .serializers import todoserializer

class ListTodo(generics.ListAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = todoserializer

class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = todoserializer
