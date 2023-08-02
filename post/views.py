from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework import filters, status, viewsets
from post.models import User, Post, Comment
from post.serializers import UserSerializer, PostSerializer, CommentSerializer
from demoProject.common.paginatiton import CustomPageSizePagination


# TEMPLATE
def index(request):
    return render(request, "postlist.html", {})


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, "post.html", {"post": post})


# API
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = CustomPageSizePagination
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['username']


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = CustomPageSizePagination
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['created_at', 'view', 'like']

    def get_queryset(self):
        queryset = Post.objects.all()
        if self.request.query_params.get("title", None):
            queryset = queryset.filter(title__contains=self.request.query_params.get("title"))
        return queryset


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = CustomPageSizePagination
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['created_at', 'updated_at']
