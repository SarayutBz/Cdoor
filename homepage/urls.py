from . import views
from django.urls import path

urlpatterns = [
    path('', views.home,name='home'),
    path('condo/', views.condo,name='condo'),
]
