from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import (ReadOnlyModelViewSet,
                                     ModelViewSet)

from .serializers import (FollowSerializer,
                          PostSerializer,
                          GroupSerializer,
                          CommentSerializer)
from .permissions import IsAuthor
from posts.models import Post, Group


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsAuthor]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsAuthor]

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
    permission_classes = [IsAuthenticated]
