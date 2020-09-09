from django.contrib import admin
from .models import Category, Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','author', 'description', 'pub_date')
    list_filter = ('title', 'category',  'pub_date',)
    search_fields = ['title', 'category__name',]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name',]

