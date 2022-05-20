from django.urls import path

from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.index),
    path('<int:pk>/', views.detail),
    path('search/', views.search),
    path('add/', views.add),
    path('<int:pk>/edit/', views.edit),
    path('<int:pk>/delete/', views.delete),
]
