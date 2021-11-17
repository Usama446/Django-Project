from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('',views.blogHome, name="bloghome"),
    path('<str:slug>',views.blogPost, name="blogPost"),
]
