from django.shortcuts import render
from rest_framework import viewsets # all CRUD
from todoapp.models import TodoListModel
from todoapp.serializers import TodoListModelSerializer

# Create your views here.
class TodoListapis(viewsets.ModelViewSet):
    queryset = TodoListModel.objects.all()
    serializer_class = TodoListModelSerializer