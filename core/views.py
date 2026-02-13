from rest_framework import viewsets
from .models import Follow
from .serializers import FollowSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Post, CustomUser
from .serializers import PostSerializer, UserSerializer
from rest_framework.exceptions import PermissionDenied


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

# Only allow users to see their own profile
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    def perform_update(self, serializer):
        if self.request.user != self.get_object().author:
            raise PermissionDenied("You cannot edit someone else's post.")
        serializer.save()

    def perform_destroy(self, instance):
        if self.request.user != instance.author:
            raise PermissionDenied("You cannot delete someone else's post.")
        instance.delete()

        # Only allow users to see posts from people they follow
class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        if self.request.user == serializer.validated_data['following']:
            raise PermissionDenied("You cannot follow yourself.")
        serializer.save(follower=self.request.user)

    def get_queryset(self):
        return Follow.objects.filter(follower=self.request.user)