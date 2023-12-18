from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('get/', views.get_cookie),
    path('delete/', views.del_cookie),
    path('set-session/', views.set_session),
    path('get-session/', views.get_session),
    path('delete-session/', views.delete_session),
]
