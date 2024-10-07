from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('service/', views.service, name='service'),
    path('prizes/', views.prizes, name='prizes'),
]