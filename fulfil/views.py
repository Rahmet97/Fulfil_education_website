from django.shortcuts import render,redirect
from django.contrib import messages
from .models import English
from .forms import EnglishForm,SMMCourseForm,FrontendForm,BackendForm,PythonForm,AndroidForm




# bu qism english registratsiya uchun
def english_form(request):
   
    form = EnglishForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Muvaffaqiyatli o'tdingiz")
        return redirect('english')
    else:
        messages.info(request, "Iltimos formani to'ldiring")    
        form = EnglishForm()
    context = {'form':form}
    return render(request,'english.html',context) 


# bu qism course
def course_list(request):

    return render(request,'cources.html')


# SMM course
def smm_course(request):
   
    form = SMMCourseForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Muvaffaqiyatli o'tdingiz")
        return redirect('smm')
    else:
        messages.info(request, "Iltimos formani to'ldiring")    
        form = SMMCourseForm()
    context = {'form':form} 
    return render(request, 'smm.html',context)       


# Frontend uchun
def frontend_course(request):
    
    form = FrontendForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Muvaffaqiyatli o'tdingiz")
        return redirect('frontend')
    else:
        messages.info(request, "Iltimos formani to'ldiring")    
        form = FrontendForm()
    context = {'form':form} 
    return render(request, 'Frontend.html',context) 



# Backend uchun
def backend_course(request):
    
    form = BackendForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request , "Muvaffaqiyatli o'tdingiz")
        return redirect('backend')
    else:
        messages.info(request, "Iltimos formani to'ldiring")    
        form = BackendForm()
    context = {'form':form}
    return render(request, 'backend.html',context)  



# Python uchun
def python_course(request):
    
    form = PythonForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Muvaffaqiyatli o'tdingiz") 
        return redirect('python')
    else:
        messages.info(request, "Iltimos formani to'ldiring")    

        form = PythonForm()
    context = {'form':form}
    return render(request,'python.html',context)        



# Android uchun
def android_course(request):
   
    form = AndroidForm(request.POST )
    if form.is_valid():
        form.save()
        messages.success(request, "Muvaffaqiyatli o'tdingiz")
        return redirect('android')
    else:
        messages.info(request, "Iltimos formani to'ldiring")            
        form = AndroidForm()
    context = {'form':form}
    return render(request, 'android.html',context)        