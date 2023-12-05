from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import *
from .models import *
from rest_framework import viewsets, permissions, status


def index(request):
    forums = Forum.objects.all()
    return render(request, 'index.html', {'forums': forums})


class ForumApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    # get all forum posts data
    def get(self, request, *args, **kwargs):  # get list of posts WORKS ----------
        posts = Forum.objects
        serializer = ForumSerializer(posts, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):  # add new post WORKS
        data = {
            'title': request.data.get('title'),
            'description': request.data.get('description'),
            'user': request.user.id,
        }

        serializer = ForumSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# from my po2

class PostApiView(APIView):
    def get(request, *args, **kwargs):  # get list of posts WORKS ----------
        posts = Post.objects
        serializer = PostSerializer(posts, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):  # add new post WORKS
        data = {
            'title': request.data.get('title'),
            'description': request.data.get('description'),
            # 'img': request.data.get('img'),
            'user': request.user.id  # user who's logged in is the one whose id is automatically placed
        }

        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetailView(APIView):  # get specific post. add request.user.id if want to make it view by same account only
    def get_obj(self, post_id):
        try:
            return Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return None

    def get(self, request, post_id, *args, **kwargs):  # based on id, grab the info. needs get_obj() from above WORKS --
        post_instance = self.get_obj(post_id)
        if not post_instance:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = PostSerializer(post_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, post_id, *args, **kwargs):  # update post by the id WORKS -------
        post_instance = self.get_obj(post_id)
        if not post_instance:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        data = {
            'title': request.data.get('title', post_instance.title),  # optional for user to edit fields
            'description': request.data.get('description', post_instance.description),
            'img': request.data.get('img', post_instance.img)
        }

        if 'img' not in request.data:  # lets me update and not get error because didn't put an img
            del data['img']

        serializer = PostSerializer(instance=post_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, post_id, *args, **kwargs):  # deletes the post WORKS ----------
        post_instance = self.get_obj(post_id)
        if not post_instance:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        post_instance.delete()

        return Response(status=status.HTTP_200_OK)


# class PostApiView(APIView):
#     def get(request, *args, **kwargs):  # get list of posts WORKS ----------
#         posts = Post.objects
#         serializer = PostSerializer(posts, many=True)
#
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def post(self, request, *args, **kwargs):  # add new post WORKS
#         data = {
#             'title': request.data.get('title'),
#             'description': request.data.get('description'),
#             # 'img': request.data.get('img'),
#             'user': request.user.id  # user who's logged in is the one whose id is automatically placed
#         }
#
#         serializer = PostSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#

class ForumDetailView(APIView):  # get specific forum
    def get_obj(self, forum_id):
        try:
            return Forum.objects.get(id=forum_id)
        except Forum.DoesNotExist:
            return None

    def get(self, request, forum_id, *args, **kwargs):  # based on id, grab the info. needs get_obj() from above WORKS --
        forum_instance = self.get_obj(forum_id)
        if not forum_instance:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = ForumSerializer(forum_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, forum_id, *args, **kwargs):  # update by the id WORKS -------
        forum_instance = self.get_obj(forum_id)
        if not forum_instance:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        data = {
            'title': request.data.get('title', forum_instance.title),  # optional for user to edit fields
            'description': request.data.get('description', forum_instance.description),
        }

        serializer = ForumSerializer(instance=forum_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, forum_id, *args, **kwargs):  # deletes the WORKS ----------
        forum_instance = self.get_obj(forum_id)
        if not forum_instance:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        forum_instance.delete()

        return Response(status=status.HTTP_200_OK)



# login/register user pages from original backend -----------------------------------------
# class CustomLoginView(LoginView):
#     template_name = "./template/index.html"
#     fields = '__all__'
#     redirect_authenticated_user = True
#
#     def get_success_url(self):
#         return reverse_lazy('index') #return to task page after completion
#
#
# class RegisterPage(FormView):
#     template_name = 'base/register.html'
#     form_class = UserCreationForm
#     redirect_authenticated_user = True
#     success_url = reverse_lazy('tasks')
#
#     def form_valid(self, form):
#         user = form.save()
#         if user is not None:
#             login(self.request, user)
#         return super(RegisterPage, self).form_valid(form)