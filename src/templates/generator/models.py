from django.db import models
from django.contrib.auth.models import User

class GeneratedWebsite(models.Model):
    # Liên kết với tài khoản người dùng
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Lưu chủ đề (VD: Đặt vé máy bay)
    topic = models.CharField(max_length=255)
    # Lưu code HTML do AI tạo ra
    html_content = models.TextField()
    # Tự động lưu thời gian tạo
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.topic