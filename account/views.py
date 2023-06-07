from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render

from .forms import SignupForm
from .models import User


def signup(request):

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_active = False
            user.save()

            url = f'{settings.WEBSITE_URL}/activateemail/?email={user.email}&id={user.id}'

            send_mail(
                "Please verify your email",
                f"The url for activating your account is: {url}",
                "noreply@wey.com",
                [user.email],
                fail_silently=False,
            )

        else:
            messages.error(request, 'Ошибка регистрации')

    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})


def activateemail(request):
    email = request.GET.get('email', '')
    id = request.GET.get('id', '')

    if email and id:
        user = User.objects.get(id=id, email=email)
        user.is_active = True
        user.save()

        return HttpResponse('The user is now activated. You can go ahead and log in!')
    else:
        return HttpResponse('The parameters is not valid!')