from . import views
from django.urls import path




urlpatterns = [
    path('home/', views.home, name='home'),
    path('AccountSelector/', views.AccountSelector, name='AccountSelector'),
    path('create_solo_account/', views.create_solo_account, name='create_solo_account'),
    path('create_organization_account/', views.create_organization_account, name='create_organization_account/'),
    path('login/', views.login, name='login'),
]