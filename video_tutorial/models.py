from django.db import models
from django.shortcuts import reverse
# Create your models here.


class CourseCategory(models.Model):
    category_image       = models.ImageField(upload_to="video_category/%Y/%m/%d/", blank=True, null=True, verbose_name='Kategoriya Rasmi:',)
    category_name        = models.CharField(max_length=200, verbose_name="Kategoriya Nomi:", unique=True)
    category_description = models.TextField(verbose_name="Kategoriya Tarifi:")

    class Meta:
        # ordering            = ['category_name']
        verbose_name        = "Kategoriya:"
        verbose_name_plural = "Kategoriyalar:"
    
    def __str__(self):
        return self.category_name

class VideoCourse(models.Model):
    video_category  = models.ForeignKey(CourseCategory, on_delete=models.CASCADE, related_name="video_name", verbose_name="Video Kategoriyasi:")
    video_url       = models.URLField(max_length=300, verbose_name="YouTube Video Linki:", ) #unique=True
    video_name      = models.TextField(verbose_name="Video Nomi:")
    video_published = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering            = ['video_published']
        verbose_name        = 'Video:'
        verbose_name_plural = 'Videolar:'

    def __str__(self):
        return self.video_name

    
    def get_absolute_url(self):
        return reverse("Products:product-detail", kwargs={"id": self.id})

