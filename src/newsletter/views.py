from django.http import HttpResponse
from django.shortcuts import render

from .forms import SignUpForm
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
