from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logoutuser, name='logoutuser'),
    path('login', views.loginuser, name='loginuser'),

    path('technology', views.technology, name='technology'),
    path('business', views.business, name='business'),
]