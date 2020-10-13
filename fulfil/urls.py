from django.urls import path
from . import views

urlpatterns = [
    path('english/', views.english_form, name="english"),
    path('cources/',views.course_list, name="cources"),
    path('smm_course/',views.smm_course, name="smm"),
    path('frontend/',views.frontend_course, name="frontend"),
    path('backend/',views.backend_course, name="backend"),
    path('python/',views.python_course, name="python"),
    path('android/', views.android_course, name="android"),
]    