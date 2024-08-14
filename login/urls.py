from . import views
from django.urls import path
from .views import login

urlpatterns = [
    path('login/', views.login,name='login'),
   
]
