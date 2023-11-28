from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.contact),
    path('practice/', views.practice),
]
