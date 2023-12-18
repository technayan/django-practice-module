from django.urls import path
from . import views

urlpatterns = [
    # path('add-post/', views.add_post, name = 'add_post'),
    path('add-post/', views.AddPostView.as_view(), name = 'add_post'),
    # path('edit-post/<int:id>/', views.edit_post, name = 'edit_post'),
    path('edit-post/<int:id>/', views.EditPostView.as_view(), name = 'edit_post'),
    path('post-details/<int:id>/', views.PostDetailsView.as_view(), name = 'post_details'),
    # path('delete-post/<int:id>/', views.delete_post, name = 'delete_post'),
    path('delete-post/<int:id>/', views.DeletePostView.as_view(), name = 'delete_post')
]