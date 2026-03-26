from django.urls import path
from .views import generator_view, website_content_view

urlpatterns = [
    path('', generator_view, name='generator_view'),
    path('content/<int:pk>/', website_content_view, name='website_content'),
]
