from django.http import HttpResponse
from django.shortcuts import render

from .forms import SignUpForm, ContactForm
from .models import SignUp


# Create your views here.


def home(request):
    form = SignUpForm(request.POST or None)
    signup_title = "Sign Up Here"

    receivers = SignUp.objects.all()

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        signup_title = "Thank you!"

    context = {
        "form": form,
        "receivers": receivers,
        "signup_title": signup_title,
    }
    template = "home.html"
    return render(request, template, context)


def contact(request):
    form = ContactForm(request.POST or None)
    contact_title = "Contact Us Here"

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        contact_title = "Sent!"

        """
        for key, value in form.cleaned_data.iteritems():
            print key, value
            # print form.cleaned_data.get(key)
        """

    context = {
        "contact_title": contact_title,
        "form": form,
    }
    template = "contact.html"

    return render(request, template, context)
