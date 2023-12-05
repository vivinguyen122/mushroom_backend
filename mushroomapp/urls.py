from django.urls import path, include
from mushroomapp import views

urlpatterns = [

    # my po2 test
    path('api/forums/', views.ForumApiView.as_view(), name='forum-api-view'),  # show api page w all forums
    path('api/posts/', views.PostApiView.as_view(), name='posts-api-view'),  # show api page w all posts

    path('api/posts/<int:post_id>/', views.PostDetailView.as_view(), name='posts-detail-api-view'),  # show api page w all posts

    path('', views.index, name='index-view'),  # show index page


]