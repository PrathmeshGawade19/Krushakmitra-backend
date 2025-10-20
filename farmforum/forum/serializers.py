from rest_framework import serializers
from .models import Category, SubCategory, Topic, Comment, CropPost
from django.contrib.contenttypes.models import ContentType

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'



class CommentSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)

    # To specify which object (topic or crop) this comment belongs to
    content_type = serializers.CharField(write_only=True)
    object_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'user', 'comment_text', 'created_at', 'content_type', 'object_id']

        
class TopicSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    subcategory_name = serializers.CharField(source='subcategory.name', read_only=True)
    category_name = serializers.CharField(source='subcategory.category.name', read_only=True)

    class Meta:
        model = Topic
        fields = ['id', 'user', 'title', 'content', 'subcategory', 'subcategory_name', 'category_name', 'created_at']



class CropPostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    image = serializers.ImageField(required=False)

    class Meta:
        model = CropPost
        fields = '__all__'
