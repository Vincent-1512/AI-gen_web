from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('generator.urls')), # Link trang chủ vào app generator
    path('accounts/', include('django.contrib.auth.urls')),
]