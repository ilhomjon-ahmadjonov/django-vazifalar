from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (signup_view,login_view,profile_view,profile_update_view,password_change_view,logout_view)

urlpatterns = [
    path('auth/signup/', signup_view, name='signup'),
    path('auth/login/', login_view, name='login'),
    path('auth/profile/', profile_view, name='profile'),
    path('auth/profile/update/', profile_update_view, name='profile_update'),
    path('auth/password-change/', password_change_view, name='password_change'),
    path('auth/logout/', logout_view, name='logout'),
]