from django.db import models
from django.shortcuts import reverse
# Create your models here.

# Blog section goes here 
class News(models.Model):
    blog_image = models.ImageField(upload_to="blog/%Y/%m/%d/", blank=True, null=True, verbose_name='Blog Rasmi:',) 
    blog_url         = models.URLField(max_length=300, verbose_name="Telegram Linki:") # telegram post link is given
    blog_description = models.TextField(verbose_name="Blog Tarifi:")
    blog_published   = models.DateTimeField(auto_now_add=True) # news published time
    blog_updated     = models.DateTimeField(auto_now=True) # news updated time

    class Meta:
        ordering            = ['blog_published', 'blog_updated'] 
        verbose_name        = "Blog"
        verbose_name_plural = "Bloglar"
    
    def __str__(self):
        return f"{self.blog_url}"


# Aloqa section goes here
# class Aloqa(models.Model):
#     pass