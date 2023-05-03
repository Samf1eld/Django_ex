from django.urls import path

from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:article_id>/', views.detail, name = 'detail'),
    path('<int:article_id>/leave_comment/', views.leave_comment, name = 'leave_comment'),
    path('/new_article/', views.new_article, name = 'new_article'),
    path('/new_article_detail/', views.new_article_detail, name = 'new_article_detail'),
    path('/new_article_detail/new_article_create/', views.new_article_create, name = 'new_article_create'),
]