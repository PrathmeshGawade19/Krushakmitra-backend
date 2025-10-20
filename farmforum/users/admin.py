from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_farmer', 'is_admin', 'is_staff', 'is_superuser')
    list_filter = ('is_farmer', 'is_admin', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email')
