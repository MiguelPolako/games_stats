"""games_stats URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from games import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Index.as_view()),
    path('games/', views.GamesView.as_view()),
    path('games/add', views.GamesAddView.as_view()),
    path('game/<int:pk>/update', views.GameUpdateView.as_view()),
    path('genres/', views.GenreView.as_view()),
    path('genres/add', views.GenreAddView.as_view()),
    path('genre/<int:id>', views.GenreDetail.as_view()),
    path('genre/<int:pk>/update', views.GenreUpdateView.as_view()),
    path('publishers/', views.PublisherView.as_view()),
    path('publishers/add', views.PublisherAddView.as_view()),
    path('publisher/<int:id>', views.PublisherDetail.as_view()),
    path('publisher/<int:pk>/update', views.PublisherUpdateView.as_view()),
    path('platforms/', views.PlatformView.as_view()),
    path('platforms/add', views.PlatformAddView.as_view()),
    path('platform/<int:id>', views.PlatformDetail.as_view()),
    path('platform/<int:pk>/update', views.PlatformUpdateView.as_view()),
    path('game/<int:id>', views.GameDetail.as_view()),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
]
