from django.urls import path
from .views import SignUpView,LoginView,ProfileView,TokenRefresh,LogoutView

urlpatterns = [
    
    path('signup/', SignUpView.as_view()),
    path('login/', LoginView.as_view()),
    path('me/', ProfileView.as_view()),
    path('token-refresh/', TokenRefresh.as_view()),
    path('logout/', LogoutView.as_view()),
]