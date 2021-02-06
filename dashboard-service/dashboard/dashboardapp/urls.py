from django.contrib import admin
from django.urls import path
from .views import Dashboard

urlpatterns = [
    path('', Dashboard.as_view(), name='dashboard-view')
]