from django.urls import path
# from . import views
from django.conf.urls import include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import HomeView, ArtDetailView, AddPostView, DeletePostView, UpdateBlog
urlpatterns = [ 
path('',HomeView.as_view(),name="home"),
path('article/<int:pk>', ArtDetailView.as_view(), name = "article_details"),
path('add_post/', AddPostView.as_view(), name= "add_post"),
path('article/edit/<int:pk>', UpdateBlog.as_view(), name="update_post"),
path('article/<int:pk>/remove', DeletePostView.as_view(), name="delete_post")
 ] 
