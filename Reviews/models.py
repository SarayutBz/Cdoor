from django.db import models
from django.contrib.auth.models import User  # ใช้โมเดล User ของ Django

class Property(models.Model):
    # โครงสร้างของ Property ที่คุณมีอยู่แล้ว
    # ควรจะอยู่ในแอพพลิเคชันอื่นหรือในแอพเดียวกันนี้
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    # เพิ่มฟิลด์อื่น ๆ ตามต้องการ

    def __str__(self):
        return self.name

class Review(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review {self.id} by {self.user.username}'

