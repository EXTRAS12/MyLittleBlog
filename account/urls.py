from django.urls import path

from .views import activateemail, signup

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('activateemail/', activateemail, name='activateemail'),
]