from django.urls import path
from . import views

urlpatterns = [
    path('', views.daily_reading, name='daily_reading'),
]
