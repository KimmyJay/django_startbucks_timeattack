from django.urls import path
from . import views

urlpatterns = [
    path('', views.category, name='category'),
    path('<str:name>/', views.detail, name='detail'),

]
