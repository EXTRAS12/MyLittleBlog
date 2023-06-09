from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import Login, activateemail, signup

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('activateemail/', activateemail, name='activateemail'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]