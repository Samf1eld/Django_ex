from django.urls import path

from . import views

app_name = 'openai'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:question_id>/', views.detail, name = 'detail'),
    path('<int:question_id>/back2main/', views.back2main, name = 'back2main'),
    path('/new_question/', views.new_question, name = 'new_question'),
    path('/new_question_detail/', views.new_question_detail, name = 'new_question_detail'),
    path('/new_question_detail/new_question_ask/', views.new_question_ask, name = 'new_question_ask'),
]