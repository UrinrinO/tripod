from django import forms
from station.models import Employee
from django.contrib.auth import get_user_model

User = get_user_model()

# class ContactForm(forms.ModelForm):
#     class Meta:
#         model = Employee
#         fields = ('first_name', 'surname', 'phone', 'email' )

class ContactForm(forms.Form):

    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "First Name"
            }
        )
    )

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Last Name"
            }
        )
    )

    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter Phone Number"
            }
        )
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Email Address"
            }
        )
    )
