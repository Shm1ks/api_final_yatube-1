from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenVerifyView,
                                            TokenRefreshView)

from .views import CommentViewSet, GroupViewSet, PostViewSet, FollowViewSet

router = routers.DefaultRouter()

router.register(r'posts', PostViewSet, basename='posts')
router.register(r'groups', GroupViewSet, basename='group')
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)
router.register(r'follow', FollowViewSet, basename='follow')

jwt_patterns = [
    path(
        'jwt/create/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path(
        'jwt/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'),
    path(
        'jwt/verify/',
        TokenVerifyView.as_view(),
        name='token_verify'),
]

urlpatterns = [
    path('v1/', include(jwt_patterns)),
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
