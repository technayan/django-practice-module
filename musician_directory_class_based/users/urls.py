from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegistrationView.as_view(), name = 'register'),
    path('login/', views.UserLoginView.as_view(), name = 'login'),
    path('logout/', views.UserLogoutView.as_view(), name = 'logout'),
    path('profile/<str:username>/', views.ProfileView.as_view(), name = 'profile'),
]