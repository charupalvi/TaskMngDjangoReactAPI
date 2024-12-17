"""
todolist app urls
"""
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from todoapp.views import TodoListapis

router = DefaultRouter()
router.register(r'todoapi',TodoListapis)

urlpatterns = [
    path('',include(router.urls))
]
