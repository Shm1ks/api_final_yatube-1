from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenVerifyView,
                                            TokenRefreshView)

from .views import CommentViewSet, GroupViewSet, PostViewSet, FollowViewSet

v1_router = routers.DefaultRouter()

v1_router.register(r'posts', PostViewSet, basename='posts')
v1_router.register(r'groups', GroupViewSet, basename='group')
v1_router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)
v1_router.register(r'follow', FollowViewSet, basename='follow')

jwt_patterns = [
    path(
        'create/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path(
        'refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'),
    path(
        'verify/',
        TokenVerifyView.as_view(),
        name='token_verify'),
]

urlpatterns = [
    path('v1/jwt/', include(jwt_patterns)),
    path('v1/', include(v1_router.urls)),
]
