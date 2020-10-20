from django.urls import path, include

from .views import (
    VideoTutorialCategory,
    VideoTutorial,
)

app_name = 'Videos'

urlpatterns = [
    path('', VideoTutorialCategory.as_view(), name="video-category"),
    path('freecourse/<int:id>', VideoTutorial.as_view(), name="video-course"),

]