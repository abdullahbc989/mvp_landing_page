from django import forms
from django.forms import ValidationError
from .models import SignUp


class ContactForm(forms.Form):
    full_name = forms.CharField(max_length=120)
    email = forms.EmailField()
    message = forms.CharField(max_length=200)


class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = [
            'full_name',
            'email',
        ]

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_base, provider = email.split("@")

        domain, extension = provider.split('.')

        domains = ['gmail', 'outlook', 'yahoo']
        extensions = ['edu', 'com', 'org']

        if domain not in domains:
            raise ValidationError("Please use an accepted email domain")
        if extension not in extensions:
            raise ValidationError("Please use an accepted email extension")

        return email

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')

        return full_name
