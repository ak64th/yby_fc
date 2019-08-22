from rest_framework import viewsets, filters

from .models import Post
from .serializers import PostSerializer


class PostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.filter(published=True)
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
