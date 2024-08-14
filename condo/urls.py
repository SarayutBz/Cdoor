# registerPage/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('condo/', views.condo, name='condo'),
]
