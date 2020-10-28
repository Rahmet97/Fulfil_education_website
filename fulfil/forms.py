from django import forms

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