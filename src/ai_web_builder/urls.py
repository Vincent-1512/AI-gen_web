from django.contrib import admin
from django.urls import path, include

# THÊM 3 DÒNG NÀY VÀO ĐỂ ĐỔI TÊN TRANG ADMIN
admin.site.site_header = "Hệ thống Quản trị AI Web Builder"
admin.site.site_title = "Admin Portal"
admin.site.index_title = "Chào mừng Vincent đến với trang quản lý"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('generator.urls')),
]