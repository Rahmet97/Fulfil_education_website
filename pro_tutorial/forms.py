from django import forms


class CourseForm(forms.Form):
    name         = forms.CharField(
                   max_length=25,
                   widget=forms.TextInput(
                       attrs={
                           "type": "text", 
                           "placeholder": "FISH", 
                           "class": "text",
                       }
                   )
                )
    phone_number = forms.CharField(
                   max_length=25,
                   widget=forms.TextInput(
                       attrs={
                           "type": "text", 
                           "placeholder": "Telefon raqam", 
                           "class": "tel",
                       }
                   )
                )
    email        = forms.EmailField(
                   widget=forms.TextInput(
                       attrs={
                           "type": "email", 
                           "placeholder": "Email",
                           "name": "email",
                           "class": "email",
                       }
                   )
                )
