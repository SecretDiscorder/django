
from django.urls import path
from . import views

urlpatterns = [
    path('', views.download, name='download'),
    
    path('chatbot/', views.chatbot, name='chatbot'),
    # Tambahkan URL pattern lainnya di sini jika ada
]
# bima/urls.py
