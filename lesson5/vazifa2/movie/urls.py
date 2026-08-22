from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import MovieCRUDView

router = DefaultRouter()

router.register(r'movie',MovieCRUDView,basename='movie')

urlpatterns = [
    path('api/', include(router.urls)),
]
