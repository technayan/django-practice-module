from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('about/', views.About, name='about'),
    path('form/', views.Form, name='form'),
    path('django-form/', views.Django_form, name='django-form'),
    path('password-validation/', views.PasswordValidationProject, name='password-validation'),
]
