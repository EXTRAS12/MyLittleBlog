from django import forms

from .models import NewsletterUser


class NewsletterUserSignupForm(forms.ModelForm):
    class Meta:
        model = NewsletterUser
        fields = ['email', ]

        def clean_email(self):
            email = self.cleaned_data.get('email')
            return email