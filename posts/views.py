from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet

from posts.models import Post
from posts.permissions import IsAuthorOrReadOnly
from posts.serializers import UserSerializer, PostSerializer


class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class PostViewSet(ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly, )
    queryset = Post.objects.all()
    serializer_class = PostSerializer
