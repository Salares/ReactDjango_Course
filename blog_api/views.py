from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer

class PostList(generics.ListCreateAPIView):
    queryset = Post.postobjects.all()
    pass

class PostDetail(generics.RetrieveDestroyAPIView):
    pass