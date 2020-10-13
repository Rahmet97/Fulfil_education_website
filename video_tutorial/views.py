from django.http import HttpResponse, Http404, HttpRequest
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404

from django.core.paginator import Paginator

from django.views import View
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    CreateView,
    DetailView,
)


from .models import (
    CourseCategory,
    VideoCourse,
)

# Create your views here.

class VideoTutorialCategory(View):
    template_name='video_tutorial/freecourses.html'
    context = {}
    queryset = None
    def get(self, request, *args, **kwargs):
        self.queryset = get_list_or_404(CourseCategory)
        self.context['object_list'] = self.queryset
        return render(
            request,
            self.template_name,
            self.context
        )


class VideoTutorial(View):
	template_name='video_tutorial/video-course.html'
	context={}
	model=CourseCategory
	look_up='id'
	def get_object(self):
		id=self.kwargs.get(self.look_up)
		
		queryset_video_list    = VideoCourse.objects.all()
		queryset_category_list = CourseCategory.objects.all()

		if id is not None:
			queryset_category     = get_object_or_404(self.model, id=id)
			queryset_video_list	  = queryset_category.video_name.all()

		return queryset_category, queryset_video_list

	def get(self, request, id=None, *args, **kwargs):
		
		video_object_list  = None
		category_object    = None
	
		category_object, video_list = self.get_object()

		paginator     = Paginator(video_list, 9)
		page_num      = paginator.num_pages
		page_indexes  = [x for x in range(1, page_num + 1)]
	
		page_number 		= request.GET.get('page')
		video_object_list   = paginator.get_page(page_number)

		self.context['video_object_list'] = video_object_list
		self.context['category_object']   = category_object
		self.context['page_indexes']      = page_indexes
		
		return render(
            request,
            self.template_name,
            self.context
        )