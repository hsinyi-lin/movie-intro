"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include

import utils.users
from movies import views as movie_views
from utils import users

admin.site.site_title = '電影後台'
admin.site.site_header = '電影後台管理'

urlpatterns = [
    path('', lambda request: redirect('/movies/')),
    path('movies/', include('movies.urls')),
    path('login/', users.login),
    path('logout/', users.logout),
    path('register/', users.register),
    path('admin/', admin.site.urls),
]

handler403 = 'utils.handlers.permission_denied'
handler404 = 'utils.handlers.not_found'
