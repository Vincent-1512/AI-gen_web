from django.contrib import admin
from .models import GeneratedWebsite

# Đăng ký Bảng vào trang Admin
@admin.register(GeneratedWebsite)
class GeneratedWebsiteAdmin(admin.ModelAdmin):
    # Các cột sẽ hiển thị trên bảng quản trị
    list_display = ('topic', 'user', 'created_at')
    # Thêm thanh tìm kiếm theo chủ đề
    search_fields = ('topic',)
    # Thêm bộ lọc bên tay phải theo người dùng và ngày tạo
    list_filter = ('user', 'created_at')
    # Sắp xếp theo ngày tạo giảm dần
    ordering = ('-created_at',)