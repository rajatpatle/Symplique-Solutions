from django.urls import path
from . import views

urlpatterns = [
    path('get-reminders', views.get_reminders, name='get_reminders'),
    path('upsert-reminders', views.upsert_reminder, name='get_reminders'),
    # Add more URL patterns for other views if needed
]
