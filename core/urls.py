from rest_framework.routers import DefaultRouter
from .views import PostViewSet, UserViewSet,FollowViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)
router.register(r'follows', FollowViewSet)

urlpatterns = router.urls
