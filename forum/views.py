from rest_framework import viewsets, permissions
from .models import Category, SubCategory, Topic, Comment, CropPost
from .serializers import (
    CategorySerializer,
    SubCategorySerializer,
    TopicSerializer,
    CommentSerializer,
    CropPostSerializer,
)
from django.contrib.contenttypes.models import ContentType
from rest_framework import viewsets, permissions
from .models import Topic, CropPost, Comment
from .serializers import CommentSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]


class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    permission_classes = [permissions.AllowAny]


class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all().order_by('-created_at')
    serializer_class = TopicSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        content_type = self.request.query_params.get("type")
        object_id = self.request.query_params.get("id")
        if content_type and object_id:
            ct = ContentType.objects.get(model=content_type)
            return Comment.objects.filter(content_type=ct, object_id=object_id)
        return Comment.objects.none()

    def perform_create(self, serializer):
        model = self.request.data.get("content_type")
        obj_id = self.request.data.get("object_id")
        ct = ContentType.objects.get(model=model)
        serializer.save(user=self.request.user, content_type=ct, object_id=obj_id)


class CropPostViewSet(viewsets.ModelViewSet):
    queryset = CropPost.objects.all().order_by('-created_at')
    serializer_class = CropPostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
