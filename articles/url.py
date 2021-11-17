from django.urls import path, re_path

from . import views

urlpatterns = [
    path('<slug:slug>/', views.DetailedArticleView.as_view()),
    path('<slug:slug>/comments/', views.CommentCreateView.as_view()),
]