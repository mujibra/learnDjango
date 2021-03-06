from django.urls import URLPattern, path, include
from . import views
from django.contrib import admin

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('register/', views.registerPage, name='register'),
    path('', views.home, name='home'),
    path('room/<str:pk>/', views.room, name='room'),
    path('profile/<str:pk>/', views.userProfile, name='profile'),
    path('create/', views.createRoom, name='create'),
    path('update/<str:pk>/', views.updateRoom, name='update'),
    path('delete/<str:pk>/', views.deleteRoom, name='delete'),
    path('delete_message/<str:pk>/', views.deleteMessage, name='delete_message'),
]