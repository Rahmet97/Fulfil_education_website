from django.contrib.auth.forms import forms
from django.forms import ModelForm
from .models import English,Smm_course,Frontend,Backend,Python,Android
from django.forms.widgets import Widget
from django.utils.translation import ugettext_lazy as _
class EnglishForm(forms.ModelForm):
    
    class Meta:
        model = English
        fields = [
            'ism','familya','telefon_raqam','email'
        ]
        widgets = {
            'ism':forms.TextInput(attrs={'class':'form-control','placeholder':'Ism',}),
            'familya':forms.TextInput(attrs={'class':'form-control','placeholder':'Familya',}),
            'telefon_raqam':forms.NumberInput(attrs={'class':'form-control','placeholder':'Telefon raqam',}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email',})

        }

class SMMCourseForm(forms.ModelForm):
    class Meta:
        model = Smm_course
        fields = [
            'ism','familya','telefon_raqam','email'
        ]
        widgets = {
            'ism':forms.TextInput(attrs={'class':'form-control','placeholder':'Ism',}),
            'familya':forms.TextInput(attrs={'class':'form-control','placeholder':'Familya',}),
            'telefon_raqam':forms.NumberInput(attrs={'class':'form-control','placeholder':'Telefon raqam',}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email',})

        }

class FrontendForm(forms.ModelForm):
    class Meta:
        model = Frontend
        fields = [
            'ism','familya','telefon_raqam','email'
        ]
        widgets = {
            'ism':forms.TextInput(attrs={'class':'form-control','placeholder':'Ism',}),
            'familya':forms.TextInput(attrs={'class':'form-control','placeholder':'Familya',}),
            'telefon_raqam':forms.NumberInput(attrs={'class':'form-control','placeholder':'Telefon raqam',}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email',})

        }        


class BackendForm(forms.ModelForm):
    class Meta:
        model = Backend
        fields = [
            'ism','familya','telefon_raqam','email'
        ]
        widgets = {
            'ism':forms.TextInput(attrs={'class':'form-control','placeholder':'Ism',}),
            'familya':forms.TextInput(attrs={'class':'form-control','placeholder':'Familya',}),
            'telefon_raqam':forms.NumberInput(attrs={'class':'form-control','placeholder':'Telefon raqam',}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email',})

        }                


class PythonForm(forms.ModelForm):
    class Meta:
        model = Python
        fields = [
            'ism','familya','telefon_raqam','email'
        ]
        widgets = {
            'ism':forms.TextInput(attrs={'class':'form-control','placeholder':'Ism',}),
            'familya':forms.TextInput(attrs={'class':'form-control','placeholder':'Familya',}),
            'telefon_raqam':forms.NumberInput(attrs={'class':'form-control','placeholder':'Telefon raqam',}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email',})

        }
   

class AndroidForm(forms.ModelForm):
    
    class Meta:
        model = Android
        fields = [
            'ism','familya','telefon_raqam','email'
        ]
        widgets = {
            'ism':forms.TextInput(attrs={'class':'form-control','placeholder':'Ism',}),
            'familya':forms.TextInput(attrs={'class':'form-control','placeholder':'Familya',}),
            'telefon_raqam':forms.NumberInput(attrs={'class':'form-control','placeholder':'Telefon raqam',}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email',})

        }


