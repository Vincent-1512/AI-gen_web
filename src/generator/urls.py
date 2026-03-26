from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dispatch/', views.dispatch_login, name='dispatch_login'), 
]