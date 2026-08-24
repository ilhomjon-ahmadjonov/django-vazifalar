from django.urls import path
from .views import *

urlpatterns  = [
    path('lc/',FoodListView.as_view()),
    # path('dud/', FoodDetailUpdateDelete.as_view())

]