from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models

from .models import (
    ProCourseName,
    ProCourseInfo,
    Teacher,
)
# Register your models here.

class TeacherAmin(admin.ModelAdmin):
    list_display = ('teacher_name', 'teacher_info', 'teacher_image', )
    list_display_links = ('teacher_name', 'teacher_info', 'teacher_image', )
    search_fields = ('teacher_name',)
    ordering = ('teacher_name',)

    fieldsets = (
        ('O\'qtuvchi Info:', {
            'fields': (
                'teacher_image',
                'teacher_name',
                'teacher_info',
            ),
        }),
    )
    formfield_overrides = {
        models.TextField : {'widget' : TinyMCE}
    }

admin.site.register(Teacher, TeacherAmin)


class InLineProCourseInfo(admin.TabularInline):
    model = ProCourseInfo
    extra = 1
    max_num = 1

class ProCourseNameAmin(admin.ModelAdmin):
    inlines=[InLineProCourseInfo]
    list_display       = ('pro_course_image', 'pro_course_name', 'pro_course_description', )
    list_display_links = ('pro_course_image', 'pro_course_name', 'pro_course_description', )
    search_fields      = ('pro_course_name',)
    ordering           = ('pro_course_name',)

    fieldsets = (
        ('Kurs Info:', {
            'fields': (
                'pro_course_image',
                'pro_course_name',
                'pro_course_description',
            ),
        }),
    )
    formfield_overrides = {
        models.TextField : {'widget' : TinyMCE()}
    }

admin.site.register(ProCourseName, ProCourseNameAmin)