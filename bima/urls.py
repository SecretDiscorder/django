
from django.urls import path
from . import views

urlpatterns = [
    path('complex_operations/', views.complex_operations, name='complex_operations'),
    path('hasil_bunga_majemuk/', views.bunga_majemuk, name='hasil_bunga_majemuk'),
    path('bunga-majemuk/', views.bunga_majemuk, name='bunga_majemuk'),
  	path('bunga-tunggal/', views.bunga_tunggal, name='bunga-tunggal'),
  	path('hasil-bunga-tunggal/', views.bunga_tunggal, name='hasil_bunga_tunggal'),
    path('compose_function/', views.compose_functions, name='compose_functions'),
    path('result/', views.compose_functions, name='result'),
    path('', views.download, name='download'),
    path('download_video/', views.download_video, name='download_video'),
    # Tambahkan URL pattern lainnya di sini jika ada
]
# bima/urls.py
