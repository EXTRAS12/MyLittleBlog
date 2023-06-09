from django.shortcuts import render
from django.views.generic import CreateView

from .forms import NewsletterUserSignupForm
from .models import NewsletterUser


class NewsletterUserView(CreateView):
    model = NewsletterUser
    form_class = NewsletterUserSignupForm
    success_url = "/"
