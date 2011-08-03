from django.contrib import admin
from django_posterous.models import BlogPost

class BlogPostAdmin(admin.ModelAdmin):
    pass

admin.site.register(BlogPost, BlogPostAdmin)
