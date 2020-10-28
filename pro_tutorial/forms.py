from django import forms
from .models import Pupil


class CourseForm(forms.ModelForm):
        pupil_name        = forms.CharField(
                                            max_length=25,
                                            widget=forms.TextInput(
                                                attrs={
                                                     "type": "text", 
                                                     "placeholder": "F.I.SH.", 
                                                     "class": "text",
                                                     }
                                                )
                                            )
        pupil_phonenumber = forms.CharField(
                                            max_length=25,
                                            widget=forms.TextInput(
                                                attrs={
                                                     "type": "text", # type must be number 
                                                     "placeholder": "+998 __ ___ __ __", 
                                                     "class": "tel",
                                                    }
                                                )
                                            )
        pupil_email       = forms.EmailField(
                                            widget=forms.TextInput(
                                                attrs={
                                                     "type": "email", 
                                                     "placeholder": "Email",
                                                     "name": "email",
                                                     "class": "email",
                                                    }
                                                )
                                            )
        class Meta:
                model= Pupil
                fields = (
                        'pupil_name', 
                        'pupil_phonenumber', 
                        'pupil_email', 
                        'teacher_name', 
                        'course_name', 
                )

        def clean_pupil_phonenumber(self, *args, **kwargs):
            pupil_phonenumber = self.cleaned_data.get('pupil_phonenumber')
            p_all = Pupil.objects.all()
            phone_number = [p.pupil_phonenumber for p in p_all]
            if pupil_phonenumber in phone_number:
                raise forms.ValidationError('This phone-number is already exist.')
            elif not (len(str(pupil_phonenumber)) == 13 and str(pupil_phonenumber).startswith("+")):
                raise forms.ValidationError('Phone-number must consists of 13 number and format must looks like this \'+998__ ___ __ __\'.')
            return pupil_phonenumber
        
        def clean_pupil_email(self, *args, **kwargs):
            pupil_email = self.cleaned_data.get('pupil_email')
            p_all = Pupil.objects.all()
            email = [p.pupil_email for p in p_all]
            if pupil_email in email:
                raise forms.ValidationError('This email is already exist.')
            return pupil_email