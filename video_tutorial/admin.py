from django.contrib import admin
from django.db import models
from tinymce.widgets import TinyMCE

from .models import (
    CourseCategory,
    VideoCourse,
)
# Register your models here.




class InLineVideoCourse(admin.TabularInline):
    model = VideoCourse
    extra = 1
    max_num = 10

class CourseCategoryAdmin(admin.ModelAdmin):
    inlines=[InLineVideoCourse]
    list_display = [
        'category_image',
        'category_name',
        'category_description'
    ]
    list_display_links=[
        'category_image',
        # 'category_name',
        'category_description'
    ]
    list_editable=[
        # 'category_image',
        'category_name',
        # 'category_description'
    ]
    # ordering=[
    #     'category_image',
    #     'category_name',
    #     'category_description'
    # ]
    fieldsets = (
        ('Category Info', {
            "fields": (
                'category_image',
                'category_name',
                'category_description'
            ),
        }),
    )
    formfield_overrides={
        models.TextField : {'widget' : TinyMCE},
    }


class VideoCourseAdmin(admin.ModelAdmin):

    list_display=(
        'video_category',
        'video_url',
        'video_name',
        'video_published',
    )
    ordering=(
        'video_category',
        'video_published',
    )
    list_editable=(
        'video_url',
        # 'video_name',
    )
    list_display_links=(
        'video_category',
        'video_name',
        'video_published',    
    )
    search_fields=(
        'video_category',
        'video_published',       
    )
    list_filter=(
        'video_category',
        'video_published', 
    )
    fieldsets = (
        ('Video Info', {
            "fields": (
                'video_category',
                'video_url',
                'video_name',
                # 'video_published',
            ),
        }),
    )
    formfield_overrides={
        models.TextField : {'widget' : TinyMCE},
    }
    



admin.site.register(CourseCategory, CourseCategoryAdmin)
admin.site.register(VideoCourse, VideoCourseAdmin)



