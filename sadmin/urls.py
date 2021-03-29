from django.urls import path
from.import views


urlpatterns = [
    path('', views.user_login, name="login"),
    path('home/', views.home, name="home"),
    path('user_logout/', views.user_logout, name="user_logout")
]
