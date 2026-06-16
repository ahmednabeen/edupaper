from django.contrib import admin
from .models import Paper, BlogPost, Scholarship


@admin.register(Paper)
class PaperAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_published', 'created_at')
    list_filter = ('category', 'is_published')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_published', 'created_at')
    list_filter = ('category', 'is_published')
    search_fields = ('title', 'excerpt')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Scholarship)
class ScholarshipAdmin(admin.ModelAdmin):
    list_display = ('title', 'region', 'country', 'is_published', 'created_at')
    list_filter = ('region', 'country', 'is_published')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
