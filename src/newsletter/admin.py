from django.contrib import admin

from .forms import SignUpForm
from .models import SignUp

# Register your models here.


class SignUpAdmin(admin.ModelAdmin):
    # class Meta:
    #   model = SignUp
    form = SignUpForm
    list_display = ["__unicode__", "timestamp", "updated"]
    ordering = ['-timestamp']

admin.site.register(SignUp, SignUpAdmin)
