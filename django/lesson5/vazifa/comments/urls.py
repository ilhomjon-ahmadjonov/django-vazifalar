from django.urls import path
from .views import AddCommentView

urlpatterns = [
    path('add/<uuid:pk>/', AddCommentView.as_view(), name='add-comment'),
]
