from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category, SubCategory, Topic, Comment, CropPost

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'description')
    list_filter = ('category',)
    search_fields = ('name', 'category__name')

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'subcategory', 'created_at')
    list_filter = ('subcategory', 'created_at')
    search_fields = ('title', 'user__username')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'content_object', 'comment_text', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__username', 'comment_text')

@admin.register(CropPost)
class CropPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'user__username')
