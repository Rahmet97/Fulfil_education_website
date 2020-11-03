from django import forms
from pro_tutorial.models import Pupil_comment


class PupilCommentForm(forms.ModelForm):
    pupil_name   = forms.CharField(
                                   max_length=25,
                                   widget=forms.TextInput(
                                       attrs={
                                            "type": "text", 
                                            "placeholder": "F.I.SH.", 
                                            "class": "text",
                                            }
                                       )
                                   )
    pupil_image  = forms.FileField(
                                   required=False,
                                   widget=forms.FileInput(
                                       attrs={
                                            "type": "file", 
                                            "id": "filein",
                                           }
                                       ),
                                   )
    pupil_comment = forms.CharField(
                                    widget=forms.Textarea(
                                        attrs={
                                             "name": "",
                                             "id": "textarea11",
                                             "placeholder": "Fikir Mulohazalaringizni yozing....",
                                            }
                                        )
                                    )

    class Meta:
        model = Pupil_comment
        fields = (
            'pupil_name', 
            'pupil_image', 
            'pupil_comment', 
        )
    

class FeedbackForm(forms.Form):
    first_name   = forms.CharField(
                 max_length=25,
                 widget=forms.TextInput(
                        attrs={
                            'type': "text",
                            'id'  : "FullName",
                            'name': "FullName",
                            'placeholder': "Ismingizni kiriting",
                            # required
                        }
                     )
                 )
    last_name    = forms.CharField(
                 max_length=25,
                 widget=forms.TextInput(
                        attrs={
                            'type': "text",
                            'id'  : "surName",
                            'name': "surName",
                            'placeholder': "Familiyangizni kiriting",
                            # required
                        }
                     )
                 )
    email        = forms.EmailField(
                 widget=forms.EmailInput(
                        attrs={
                            'type': "email",
                            'id'  : "email",
                            'name': "email",
                            'placeholder': "Elektron pochtangizni kiriting",
                        }
                     )
                 )
    phone_number = forms.CharField(
                 max_length=13,
                 widget=forms.TextInput(
                        attrs={
                            'type': "text",
                            'id'  : "call",
                            'name': "call",
                            'placeholder': "Telefon Raqamingizni kiriting",
                            # required
                        }
                     )
                 )
    text         = forms.CharField(
                 widget=forms.Textarea(
                        attrs={
                            "name": "",
                            "placeholder" : "Fikir mulohaza va takliflaringizni kiriting"
                        }
                    )
                 )