from django.shortcuts import render
from django.http.response import HttpResponse


def register(request):
  return render(request,'register/register.html')
