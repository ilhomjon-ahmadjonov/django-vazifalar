from django.urls import path
from .views import RegisterView,home, LoginView

urlpatterns = [
    path('regis' ,RegisterView.as_view(), name= 'regis'),
    path('home' ,home, name= 'home'),
    path('login' ,LoginView.as_view(), name= 'login')
]