from . import views
from django.urls import path




urlpatterns = [
    path('home/', views.home, name='home'),
    path('create_account/', views.create_account, name='create_account'),
    path('login/', views.login, name='login'),
]