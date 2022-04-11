from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import PostViewSet, GroupView, CommentViewSet, FollowViewSet

router_v1 = DefaultRouter('v1')
router_v1.register(r'posts', PostViewSet, basename='post')
router_v1.register(r'groups', GroupView, basename='group')
router_v1.register(r'follow', FollowViewSet, basename='follow')
router_v1.register(
    r'^posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comment'
)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
