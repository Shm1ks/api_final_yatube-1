from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, permissions
from rest_framework.viewsets import (ReadOnlyModelViewSet,
                                     ModelViewSet)

from .serializers import (FollowSerializer,
                          PostSerializer,
                          GroupSerializer,
                          CommentSerializer)
from .permissions import IsAuthor
from posts.models import Post, Group, Follow


class GroupViewSet(ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    pagination_class = None


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthor]
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('group', )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthor]

    def get_post(self):
        return get_object_or_404(
            Post, id=self.kwargs.get('post_id')
        )

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user, post=self.get_post()
        )

    def get_queryset(self):
        return self.get_post().comments.all()


class FollowViewSet(ModelViewSet):
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ('user', 'following')
    search_fields = ('following__username',)
    pagination_class = None

    def get_queryset(self):
        user = self.request.user
        new_queryset = Follow.objects.filter(user=user)
        return new_queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
