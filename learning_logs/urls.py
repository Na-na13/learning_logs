"""Defines URL patterns for learning_logs."""
from django.urls import path

from . import views

urlpatterns = [
    # Home Page
    path("", views.index, name="index"),
    # Show all topics
    path("topics", views.topics, name='topics')
]
