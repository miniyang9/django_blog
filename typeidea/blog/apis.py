# from rest_framework import generics
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
#
# from .models import Post
# from .serializers import PostSerializer
#
# 函数方法
# @api_view()
# def post_list(request):
#     posts = Post.objects.filter(status=Post.STATUS_NORMAL)
#     post_serializers = PostSerializer(posts, many=True)
#     return Response(post_serializers.data)
#
# 类方法
# class PostList(generics.ListCreateAPIView):
#     queryset = Post.objects.filter(status=Post.STATUS_NORMAL)
#     serializer_class = PostSerializer

# from rest_framework import viewsets
# from rest_framework.permissions import IsAdminUser
#
# from .models import Post
# from .serializers import PostSerializer
#
#
# class PostViewSet(viewsets.ReadOnlyModelViewSet):
#     serializer_class = PostSerializer
#     queryset = Post.objects.filter(status=Post.STATUS_NORMAL)
#     # permission_classes = [IsAdminUser]    # 写入时权限检验

from rest_framework import viewsets
from .serializers import (PostSerializer, PostDetailSerializer,
                          CategorySerializer, CategoryDetailSerializer)
from .models import Post, Category


class PostViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=Post.STATUS_NORMAL)
    # permission_classes = [IsAdminUser]    # 写入时权限检验

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = PostDetailSerializer
        return super().retrieve(request, *args, **kwargs)

    def filter_queryset(self, queryset):
        category_id = self.request.query_params.get("category")
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        return queryset


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.filter(status=Category.STATUS_NORMAL)

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = CategoryDetailSerializer
        return super().retrieve(request, *args, **kwargs)


