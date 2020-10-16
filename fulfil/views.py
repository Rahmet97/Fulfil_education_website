from django.http import HttpResponse, Http404, HttpRequest, BadHeaderError
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.core.paginator import Paginator

from django.views import View


from .models import News

# Create your views here.


# Class based Home View
class Home(View):
    template_name='fulfil/index.html'
    context = {}
    def get(self, request, *args, **kwargs):
        return render(
            request,
            self.template_name,
            self.context
        )


# Class Based About View
class About(View):
    template_name='fulfil/about.html'
    context = {}
    def get(self, request, *args, **kwargs):
        return render(
            request,
            self.template_name,
            self.context
        )


# Class Based Contact View
from .forms import FeedbackForm
from django.core.mail import send_mail
from django.conf import settings
from fulfil_education import settings

class Contact(View):
    template_name='fulfil/aloqa.html'
    context = {}

    def get(self, request, *args, **kwargs):
        form = FeedbackForm()
        return render(
            request,
            self.template_name,
            self.context
        )
    def post(self, request, *args, **kwargs):
        if request.method == "POST":
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
                return redirect('FulFil:contact')
            else:
                return redirect('FulFil:contact')
        self.context = {
            'form': form
        }
        return render(
            request, 
            self.template_name,
            self.context
        )

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
            return redirect('FulFil:contact')
        else:
            return redirect('FulFil:contact')
    context = {
        'form': form
    }
    return render(request, 'fulfil/aloqa.html', context)

# Class Based Blog View
class Blog(View):
    template_name ='fulfil/blog.html'
    context       = {}
    def get(self, request, *args, **kwargs):
        news_list        = News.objects.all()
        news_object_list = None

        paginator    = Paginator(news_list, 9)
        page_num     = paginator.num_pages
        page_indexes = [x for x in range(1, page_num + 1)]
	
        page_number 	 = request.GET.get('page')
        news_object_list = paginator.get_page(page_number)

        self.context['news_list']    = news_object_list
        self.context['page_indexes'] = page_indexes
		
        return render(
            request,
            self.template_name,
            self.context
        )