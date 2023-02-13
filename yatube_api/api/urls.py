from rest_framework.routers import SimpleRouter
from django.urls import include, path

from .views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet


router = SimpleRouter()

router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='Comment'
)
router.register('follow', FollowViewSet, basename='Follow')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
