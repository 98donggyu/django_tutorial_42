from django.urls import path
from community.views import articleList, write, viewDetail 
from . import views

urlpatterns = [
    path('write/', write, name='write'),
    path('list/', articleList, name='list'),
    path('view_detail/<int:num>/', viewDetail, name='view_detail'),
    path('delete_article/<int:article_id>/', views.delete_article, name='delete_article'),
]