from django.http import HttpResponse, Http404, HttpRequest, BadHeaderError
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.contrib import messages
from django.views import View

from fulfil_education import settings
from .forms import CourseForm

from .models import (
    ProCourseName,
    ProCourseInfo,
    Teacher,
    Pupil,
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
    template_name = 'pro_tutorial/course_info.html'
    context       = {}
    model         = ProCourseName
    look_up       = 'id'

    teacher_name  = None
    course_name   = None
    
    def get_object(self):
        id = self.kwargs.get(self.look_up)

        if id is not None:
            queryset_course_name = get_object_or_404(self.model, id=id)
            queryset_course_info = queryset_course_name.payed_course_name.all()

        return queryset_course_info

    def get(self, request, id=None, *args, **kwargs):
        form            = CourseForm()
        queryset_course = None
        queryset_course = self.get_object()
        
        self.context['course_info']  = queryset_course
        self.context['form']         = form
		
        return render(
            request,
            self.template_name,
            self.context
        )

    def post(self, request, id=None, *args, **kwargs):
        # TEACHER NAME
        course     = self.get_object()
        t_name     = [c.course_teacher for c in course]
        teacher_n  = t_name[0]
        # TEACHER NAME
 
        if teacher_n:
            self.teacher_name = Teacher.objects.get(teacher_name=teacher_n) # TEACHER instance
        self.course_name  = ProCourseName.objects.get(id=id) # COURSE instance
        
        if request.method == "POST":
            form = CourseForm(request.POST)
            if form.is_valid():
                name         = form.cleaned_data['pupil_name']
                email        = form.cleaned_data['pupil_email']
                phone_number = form.cleaned_data['pupil_phonenumber']
                form.save()
                new_form = Pupil.objects.create(pupil_name=name, pupil_phonenumber=phone_number, pupil_email=email,  course_name=self.course_name, teacher_name=self.teacher_name,) # teacher_name=t_name,
                if new_form.is_valid():
                    new_form.save() # save new pupil info to the database
                else:
                    for msg in new_form.error_messages:
                        messages.error(request, f"{msg}: {form.error_messages[msg]}")
                # send_mail(name, f'{name} {self.course_name.pro_course_name} kursga qatnashmoqchi.\n Tel:{phone_number}\nEmail{email}', settings.EMAIL_HOST_USER, ['@example.com'])
                try:
                    
                    # sending email to the host
                    # send_mail(name, f'{name} {self.course_name.pro_course_name} kursga qatnashmoqchi.\n Tel:{phone_number}\nEmail{email}', settings.EMAIL_HOST_USER, ['@example.com']) 
                    # ------- HOST -------
                    
                    # sending email to the applier
                    send_mail('FulFil Education', f'siz {self.course_name} kursga yozildingiz. \nMurojat uchun: \nTel: 998683826;', settings.EMAIL_HOST_USER, email)
                    messages.success(request, f"{name} xabaringiz muvofaqiyatli yuborildi.")
                    # ------- APPLIER -------
                    
                    # new_form.save() # save new pupil info to the database

                except BadHeaderError:
                    return HttpResponse(f'Invalid header')

                return render("Pro_Tutorial:course-tutorial", id)

            else:
                for msg in form.errors:
                    messages.error(request, f"{msg} - already exist.")

        self.context = {
            'form': form
        }
        return render(
            request, 
            self.template_name,
            self.context
        )


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
