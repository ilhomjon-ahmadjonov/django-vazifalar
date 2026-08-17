from django.urls import path
from .views import CarListCreateApiView,CarDetaialDeleteUpdate

urlpatterns = [
    path('list-create/',CarListCreateApiView.as_view()),
    path('detail-update-delete/<int:pk>/',CarDetaialDeleteUpdate.as_view()),
]