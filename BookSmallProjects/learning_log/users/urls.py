from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import login
from . import views

app_name = 'users'

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('user_logout/', views.user_logout, name='user_logout')
]
