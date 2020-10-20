from django.urls import path, include

from .views import (
    Home,
    About,
    Contact,
    Blog,
)

app_name='FulFil'

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('about/', About.as_view(), name='about'),
    path('contact/', Contact.as_view(), name='contact'),
    path('blog/', Blog.as_view(), name='blog'),
]