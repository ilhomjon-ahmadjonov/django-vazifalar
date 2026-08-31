from django.urls import path
from .views import *

urlpatterns = [
    path('sigup',SignUpView.as_view()),
    path('login',LoginView.as_view()),
    path('logout',LogOutView.as_view())
]