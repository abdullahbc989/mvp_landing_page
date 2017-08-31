from django.conf import settings
from django.core.mail import send_mail
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
        form_subject = form.cleaned_data.get('subject')
        email = form.cleaned_data.get('email')
        form_message = form.cleaned_data.get('message')
        full_name = form.cleaned_data.get('full_name')

        sender = settings.EMAIL_HOST_USER

        send_mail(subject=form_subject,
                  message=form_message,
                  from_email=sender,
                  recipient_list=[sender],
                  fail_silently=False)

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
