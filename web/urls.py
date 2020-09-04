from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('blog', views.blog),
    path('blog/<str:slug>', views.blog_details),
    path('properties/', views.props),
    path('properties/<str:slug>/', views.details), 
]