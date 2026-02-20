from django.urls import path
from rest_framework.routers import DefaultRouter
from django.contrib.auth import views as auth_views
from .views import FeedView, PostViewSet, UserViewSet,FollowViewSet,home_view, register_view
from .views import profile_view
from .views import like_post

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)
router.register(r'follows', FollowViewSet)

urlpatterns = [
    path('feed/', FeedView.as_view(), name='feed'),
       path('', home_view, name='home'),
    path('register/', register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    path('profile/<str:username>/', profile_view, name='profile'),
    path('like/<int:post_id>/', like_post, name='like_post'),
] + router.urls
