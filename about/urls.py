from django.urls import path
from . import views

# Define the URL patterns for the 'about' app
urlpatterns = [
    path('', views.about_me, name='about'),
    path('create/', views.create_about_page, name='create_about_page'),
    path('edit/', views.edit_about_page, name='edit_about_page'),
    path('<str:username>/', views.view_about_page, name='view_about_page'),
]
