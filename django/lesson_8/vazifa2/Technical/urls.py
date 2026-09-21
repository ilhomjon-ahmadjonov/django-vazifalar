from django.urls import path
from .views import HomeView,TechnicalListViews,TechnicalCreateViews,TechnicalDetailViews,TechnicalDeleteViews,TechnicalUpdateViews


urlpatterns = [
    path('home', HomeView.as_view(), name='home'),
    path('list', TechnicalListViews.as_view(), name='list'),
    path('create', TechnicalCreateViews.as_view(), name='create'),
    path('detail/<int:pk>/', TechnicalDetailViews.as_view(), name='detail'),
    path('update/<int:pk>/', TechnicalUpdateViews.as_view(), name='update'),
    path('delete/<int:pk>/', TechnicalDeleteViews.as_view(), name='delete'),

]