from django.urls import path
from .views import index, teachers, course_list, course_detail

urlpatterns = [
    path('', index, name='home'),
    path('teachers/', teachers, name='teachers'),
    path('courses/', course_list, name='courses'),
    path('course/<int:pk>/', course_detail, name='course_detail'),
]