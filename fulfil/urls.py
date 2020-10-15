from django.urls import path
from .views import index, teachers, course_list, course_detail, feedback

urlpatterns = [
    path('', index, name='home'),
    path('teachers/', teachers, name='teachers'),
    path('courses/', course_list, name='courses'),
    path('course/<int:pk>/', course_detail, name='course_detail'),
    path('feedback/', feedback, name='feedback'),
]