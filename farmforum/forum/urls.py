from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CategoryViewSet,
    SubCategoryViewSet,
    TopicViewSet,
    CropPostViewSet,
    CommentViewSet,
)

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'subcategories', SubCategoryViewSet, basename='subcategory')
router.register(r'topics', TopicViewSet, basename='topic')
router.register(r'comments', CommentViewSet, basename='comment')
router.register(r'crops', CropPostViewSet, basename='croppost')

urlpatterns = [
    path('', include(router.urls)),
]
