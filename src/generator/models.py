from django.db import models
from django.contrib.auth.models import User

class GeneratedWebsite(models.Model):
    """
    Model để lưu trữ một trang web được tạo ra bởi AI.
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="generated_websites",
        verbose_name="Người dùng"
    )
    topic = models.CharField(
        max_length=255,
        verbose_name="Chủ đề"
    )
    generated_content = models.TextField(
        verbose_name="Nội dung do AI tạo"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Ngày tạo"
    )

    def __str__(self):
        return f"'{self.topic}' cho {self.user.username} vào {self.created_at.strftime('%Y-%m-%d %H:%M')}"

    class Meta:
        verbose_name = "Website được tạo"
        verbose_name_plural = "Các website được tạo"
        ordering = ['-created_at']
