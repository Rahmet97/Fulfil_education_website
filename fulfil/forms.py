from django import forms


class CourseForm(forms.Form):
    name = forms.CharField(max_length=25)
    phone_number = forms.CharField(max_length=25)
    email = forms.EmailField()