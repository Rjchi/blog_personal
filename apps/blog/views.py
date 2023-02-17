from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from apps.category.models import Category

from .serializers import PostSerializer
from .models import ViewCount, Post


class BlogListView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        if Post.objects.all().exists():
            print('List post')
            return Response({'Post': 'Test message'}, status=status.HTTP_200_OK)
        else:
            return Response({'Error':'Not Found'}, status=status.HTTP_404_NOT_FOUND)