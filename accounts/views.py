from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth import authenticate, login
from .forms import RegisterForm

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # เปลี่ยนเป็น URL ที่คุณต้องการให้ผู้ใช้ไปเมื่อสมัครเสร็จแล้ว
    else:
        form = RegisterForm()
    
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # แทนที่ 'home' ด้วยชื่อ URL ของหน้าหลักของคุณ
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid username or password'})
    return render(request, 'accounts/login.html')