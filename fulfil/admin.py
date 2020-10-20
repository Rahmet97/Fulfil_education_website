from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models

from .models import News

# Register your models here.

# Blog section goes here
class NewsAdmin(admin.ModelAdmin):
    list_display       = ('blog_image', 'blog_url', 'blog_published', 'blog_updated', )
    list_display_links = ('blog_image', 'blog_url')
    ordering           = ('blog_published', 'blog_updated',)

    fieldsets = (
        ('Kurs Info:', {
            'fields': (
                'blog_image',
                'blog_url',
                'blog_description',
            ),
        }),
    )
    formfield_overrides = {
        models.TextField : {'widget' : TinyMCE()}
    }

admin.site.register(News, NewsAdmin)

# aloqa section goes here
# class AloqaAdmin(admin.ModelAdmin):
#     pass


