"""
URL configuration for server project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from main import views as main
from users import views as cabinet
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main.Index, name='main'),
    path('player/auditions', main.Auditions, name='auditions'),
    path('player/like', main.Like, name='like'),
    path('player/mark audition', main.Mark_audition, name='mark audition'),
    path('player', main.Player, name='player'),
    path('author', main.Author, name='author'),
    path('search', main.Search, name='search'),
    path('login', cabinet.Login, name='login'),
    path('registration', cabinet.Registration, name='registration'),
    path('cabinet', cabinet.Cabinet, name='cabinet'),
]

handler404 = 'main.views.Page_not_found'
