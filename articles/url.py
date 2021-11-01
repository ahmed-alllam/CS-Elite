from django.urls import path

import views

urlpatterns = [
    path('(?P<tag>\w+)/', views.ArticlesByTagView.as_view()),
    path('<slug:slug>/', views.DetailedArticleView.as_view()),
    path('<slug:slug>/comments/', views.CommentCreateView.as_view()),
]