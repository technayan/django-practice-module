from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name = 'register'),
    path('login/', views.user_login, name = 'login'),
    path('profile/', views.profile, name = 'profile'),
    path('logout/', views.user_logout, name = 'logout'),
    path('change-password/', views.change_password, name = 'change_password'),
    path('set-password/', views.set_password, name = 'set_password'),
]
