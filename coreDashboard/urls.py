from . import views
from django.urls import path




urlpatterns = [
    path('home/', views.home, name='home'),
    path('createAccount/', views.createAccount, name='createAccount'),
    path('login/', views.login, name='login'),
]