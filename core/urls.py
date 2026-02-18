from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import FeedView, PostViewSet, UserViewSet,FollowViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)
router.register(r'follows', FollowViewSet)

urlpatterns = router.urls + [
    path('feed/', FeedView.as_view(), name='feed'),
]
