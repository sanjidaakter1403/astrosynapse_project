# dashboard/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('eeg-analyzer/', views.eeg_analyzer, name='eeg_analyzer'),
    path('api/simulate-eeg/', views.simulate_eeg, name='simulate_eeg'),
    path('time-perception/', views.time_perception, name='time_perception'),
    path('recommendations/', views.recommendations, name='recommendations'),
]