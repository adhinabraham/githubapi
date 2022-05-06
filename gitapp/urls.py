from django.contrib import admin

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from gitapp import views

urlpatterns = [
      path('', views.github.as_view(),), 
]