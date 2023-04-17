from django.contrib import admin
from .models import Post, PostTag

class BlogAdmin(admin.ModelAdmin):
    list_filter = ['is_active']
    list_display = ['title', 'publish_date', 'is_active']
    list_editable = ['is_active']


admin.site.register(Post, BlogAdmin)
admin.site.register(PostTag)
