from django import forms


class CourseForm(forms.Form):
    name = forms.CharField(max_length=25)
    phone_number = forms.CharField(max_length=25)
    email = forms.EmailField()


class FeedbackForm(forms.Form):
    first_name = forms.CharField(max_length=25)
    last_name = forms.CharField(max_length=25)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=25)
    text = forms.CharField(widget=forms.Textarea)

