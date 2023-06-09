from django.urls import path

from .views import NewsletterUserView

urlpatterns = [
    path('sub/', NewsletterUserView.as_view(), name='sub')
]
