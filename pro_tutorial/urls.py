from django.urls import path, include

from .views import (
    Pro_Tutorials_List,
    Course_Info,
    Teachers_List,
)

app_name = "Pro_Tutorial"

urlpatterns = [
    # Category's url
    path('', Pro_Tutorials_List.as_view(), name="tutorial-category"),
    # Courses' urls
    path('course/<int:id>/',  Course_Info.as_view(),  name="course-tutorial"),
    # Teachers' url
     path('teachers', Teachers_List.as_view(), name="teacher-list"),
]