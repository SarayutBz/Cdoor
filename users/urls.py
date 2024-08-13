# users/urls.py

from django.urls import path
from .views import UserListView, UserDetailView, CreateUserView

urlpatterns = [
    path('create/', CreateUserView.as_view(), name='create_user'),  # สำหรับ POST ผู้ใช้ใหม่
    path('', UserListView.as_view(), name='user_list'),  # สำหรับ GET รายชื่อผู้ใช้ทั้งหมด
    path('<int:user_id>/', UserDetailView.as_view(), name='user_detail'),  # สำหรับ GET ผู้ใช้เฉพาะคน
]

