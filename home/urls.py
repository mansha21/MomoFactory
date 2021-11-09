from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.popular_view, name='index'),
    path('', views.feedback_view, name='index'),
    path('', views.news_view, name='index'),
    path('', views.menu_view, name='index'),

]