from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), # Kích hoạt bộ Auth của Django
    path('', include('generator.urls')), # Trỏ trang chủ về app generator
]