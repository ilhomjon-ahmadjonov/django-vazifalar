from django.urls import path
from .views import RegisterView,home, LoginView,ProfilView,ProfileUpdateView,LogoutView

app_name = 'auth'

urlpatterns = [
    path('regis' ,RegisterView.as_view(), name= 'regis'),
    path('home' ,home, name= 'home'),
    path('login' ,LoginView.as_view(), name= 'login'),
    path('me' ,ProfilView.as_view(), name= 'me'),
    path('update' ,ProfileUpdateView.as_view(), name= 'update'),
    path('logout' ,LogoutView.as_view(), name= 'logout')
]