from django.urls import path
from .views import SignUpView,VerifyCodeView, GetNewCodeView

urlpatterns = [
    path('signup/', SignUpView.as_view()),
    path('verify/', VerifyCodeView.as_view()),
    path('new-code/', GetNewCodeView.as_view())
]