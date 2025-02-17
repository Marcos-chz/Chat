from django.contrib import admin
from django.urls import path, include
from chat import views

# Project URLs
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('chat/', include('chat.urls')),  
    path('menu/', views.menu, name='menu')
]