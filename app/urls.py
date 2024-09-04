from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('course/<slug:slug>/', views.neet, name='batch_detail'),
    path('subject/<slug:slug>/', views.chapter_list, name='chapter_list'),
    path('subject/chapter/<slug:slug>/', views.lect, name='lecture_list'),
    path('lecture/<slug:slug>/', views.lecture_detail, name='lecture_detail'),
]
