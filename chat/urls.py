from django.urls import path
from . import views

# Just 3 rooms allowed
urlpatterns = [
    path('1/', views.room, {'room_name': '1'}, name='room1'),
    path('2/', views.room, {'room_name': '2'}, name='room2'),
    path('3/', views.room, {'room_name': '3'}, name='room3'),
    path('<str:room_name>/', views.room, name='room'),  
]
