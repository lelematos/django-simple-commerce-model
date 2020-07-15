from django.contrib import admin
from django.urls import path, include
from .views import PostDetail, post_delete

appname = "posts"
urlpatterns = [
    path('<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('<int:pk>/delete/', post_delete, name='post_delete'),
]
