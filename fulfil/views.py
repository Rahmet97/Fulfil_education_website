from django.core.mail import send_mail
from django.http import BadHeaderError, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from fulfil_education import settings
from .models import Teacher, Course
from .forms import CourseForm, FeedbackForm


def index(request):
    return render(request, 'index.html')


def teachers(request):
    teachers = Teacher.objects.all()
    return render(request, 'teachers.html', {'teachers': teachers})


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'cources.html', {'courses': courses})


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


def feedback(request):
    if request.method == 'GET':
        form = FeedbackForm()
    else:
        form = FeedbackForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            text = form.cleaned_data['text']
            try:
                send_mail(f'{first_name} {last_name}', f"{text}\nTel: {phone_number}\nEmail: {email}",
                          settings.EMAIL_HOST_USER, ['example@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header')
            return redirect('home')
        else:
            return redirect('feedback')
    context = {
        'form': form
    }
    return render(request, 'aloqa.html', context)
