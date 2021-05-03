from .models import Post
from .serializer import PostSerializer
from rest_framework import generics, permissions
from .permissions import IsAuthorOrReadOnly

class PostList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly, ) 
    queryset = Post.objects.all()
    serializer_class = PostSerializer    