from django.urls import path
from .views import ListView,RegisterView,LoginView,ProfilView,ProfileUpdateView, LogOutView

app_name = 'auth'

urlpatterns = [
    path('list/',ListView.as_view(),name='list'),
    path('register/', RegisterView.as_view(),name='register'),
    path('login/',LoginView.as_view(),name='login'),
    path('profile/', ProfilView.as_view(),name='profile'),
    path('update/',ProfileUpdateView.as_view(),name='update'),
    path('logout/',LogOutView.as_view(),name='logout')         

]