from rest_framework import viewsets
from .models import Follow
from .serializers import FollowSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Post, CustomUser
from .serializers import PostSerializer, UserSerializer
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import ListAPIView
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
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


class FeedView(ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        following_users = Follow.objects.filter(
            follower=self.request.user
        ).values_list('following', flat=True)

        return Post.objects.filter(
            author__in=following_users
        ).order_by('-created_at')


@login_required
def home_view(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Post.objects.create(author=request.user, content=content)

    following_users = Follow.objects.filter(
        follower=request.user
    ).values_list('following', flat=True)

    posts = Post.objects.filter(
        author__in=following_users
    ).order_by('-created_at')

    return render(request, 'home.html', {'posts': posts})


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})

User = get_user_model()

@login_required
def profile_view(request, username):
    profile_user = get_object_or_404(User, username=username)

    # Follow / Unfollow logic
    if request.method == 'POST':
        if profile_user != request.user:
            follow, created = Follow.objects.get_or_create(
                follower=request.user,
                following=profile_user
            )
            if not created:
                follow.delete()

        return redirect('profile', username=username)

    # Stats
    followers_count = Follow.objects.filter(
        following=profile_user
    ).count()

    following_count = Follow.objects.filter(
        follower=profile_user
    ).count()

    is_following = Follow.objects.filter(
        follower=request.user,
        following=profile_user
    ).exists()

    posts = Post.objects.filter(
        author=profile_user
    ).order_by('-created_at')

    context = {
        'profile_user': profile_user,
        'followers_count': followers_count,
        'following_count': following_count,
        'is_following': is_following,
        'posts': posts
    }

    return render(request, 'profile.html', context)