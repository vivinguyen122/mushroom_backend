"""mushroomproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include, re_path
from rest_framework import routers
from mushroomapp import views, urls

# router = routers.DefaultRouter()
# router.register(r'forums', views.ForumView, 'forum')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(urls)),

    # re_path(r'^api/forms/$', views.ForumApiView.as_view()),

    re_path(r'^api/forums/$', views.forum_list), #get list of forums add add new forum
    # re_path(r'^api/forums/$', views.forum_detail), # delete forum and update forum

    # re_path(r'^api/forms/([3-4])$', views.ForumApiView.as_view()),
    # path('api/', views.ForumApiView.as_view())

    # path('api/forums/$', views.forum_list),  # get list of forums add add new forum

    # my po2 test
    path('api/forums/<int:pk>/', views.ForumDetail.as_view(), name='forum-view')
]
