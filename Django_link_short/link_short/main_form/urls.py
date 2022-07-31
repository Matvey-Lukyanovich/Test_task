from django.urls import path, include
from . import views

urlpatterns = [
    path('logout/', views.logoutUser, name="logout"),
    path('login/',views.loginPage, name = "login"),
    path('register/',views.registerPage, name = "register"),
    path('history/', views.history, name="history"),
    path('', views.home, name="home"),
]
