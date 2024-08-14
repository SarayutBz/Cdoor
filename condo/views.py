from django.shortcuts import render
from django.http.response import HttpResponse


def condo(request):
  return render(request,'condo1/condo.html')
