from django.shortcuts import render
from django.views.generic import DetailView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Forum, Post
from .serializers import *
from rest_framework import viewsets, permissions, status


def index(request):
    forums = Forum.objects.all()
    return render(request, 'index.html', {'forums': forums})


class ForumApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    # get all forum posts data
    # @api_view(['GET', 'POST'])
    def get(self, request, *args, **kwargs):
        forums = Forum.objects
        serializer = ForumSerializer(forums, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


# from my po2

class ForumDetail(DetailView):
    model = Forum
    context_object_name = 'forum'
#

@api_view(['GET', 'POST'])
def forum_list(request):
    if request.method == 'GET':

        forums = Forum.objects.all()
        serializer = ForumSerializer(forums, context={'request': request}, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = ForumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE'])
def forum_detail(request, user):
    try:
        user_num = Forum.objects.get(user=user)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ForumSerializer(user_num, data=request.data, context={'request': request}, many=True)

    if request.method == 'PUT':
        if serializer.is_valid():
            serializer.save()

            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()

        return Response(serializer.errors, status=status.HTTP_204_NO_CONTENT)
