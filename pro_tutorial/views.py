from django.http import HttpResponse, Http404, HttpRequest, BadHeaderError
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.views import View

from fulfil_education import settings
from .forms import CourseForm

from .models import (
    ProCourseName,
    ProCourseInfo,
    Teacher,
)


# Class Based Pro_Tutorials_List View
class Pro_Tutorials_List(View):
    template_name = 'pro_tutorial/cources.html'
    context       = {}

    def get(self, request, *args, **kwargs):
        video_list        = ProCourseName.objects.all()
        video_object_list = None

        paginator    = Paginator(video_list, 9)
        page_num     = paginator.num_pages
        page_indexes = [x for x in range(1, page_num + 1)]
	
        page_number 	  = request.GET.get('page')
        video_object_list = paginator.get_page(page_number)

        self.context['course_object_list'] = video_object_list
        self.context['page_indexes']	  = page_indexes
		
        return render(
            request,
            self.template_name,
            self.context
        )


# Class Based Course_Info View
class Course_Info(View):
    template_name='pro_tutorial/course_info.html'
    context={}
    model=ProCourseName
    look_up='id'
    
    def get_object(self):
        id=self.kwargs.get(self.look_up)

        if id is not None:
            queryset_course_name = get_object_or_404(self.model, id=id)
            queryset_course_info = queryset_course_name.payed_course_name.all()
            print(queryset_course_info)

        return queryset_course_info

    def get(self, request, id=None, *args, **kwargs):
        form = CourseForm()
        queryset_course = None
        queryset_course = self.get_object()

        self.context['course_info']  = queryset_course
        self.context['form']  = form
		
        return render(
            request,
            self.template_name,
            self.context
        )

    def post(self, request, id=None, *args, **kwargs):
        course = ProCourseName.objects.get(id=id)
        if request.method == "POST":
            form = CourseForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                phone_number = form.cleaned_data['phone_number']
                try:
                    send_mail(name,
                          f'{name} {course.pro_course_name} kursga qatnashmoqchi.\n Tel:{phone_number}\nEmail{email}',
                          settings.EMAIL_HOST_USER, ['@example.com'])
                except BadHeaderError:
                    return HttpResponse('Invalid header')
                return redirect('Pro_Tutorial:course-tutorial', id )
            else:
                return redirect('Pro_Tutorial:course-tutorial', id )
        self.context = {
            'form': form
        }
        return render(
            request, 
            self.template_name,
            self.context
        )

"""
def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'GET':
        form = CourseForm()
    else:
        form = CourseForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            try:
                send_mail(name,
                          f'{name} {course.teacher}ning {course.title} kursiga qatnashmoqchi.\n Tel:{phone_number}\nEmail{email}',
                          settings.EMAIL_HOST_USER, ['@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header')
            return redirect('home')
        else:
            return redirect('course_detail')
    context = {
        'course': course,
        'form': form
    }
    return render(request, 'course_detail.html', context)

"""




# Class Based Teachers View
class Teachers_List(View):
    template_name='teachers/teachers.html'
    context = {}

    def get_object(self):
        queryset = Teacher.objects.all()
        return queryset
    
    def get(self, request, *args, **kwargs):
        self.context["teachers_list"] = self.get_object()
        return render(
            request,
            self.template_name,
            self.context
        )
