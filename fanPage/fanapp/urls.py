from django.urls import path
from .views import *

urlpatterns = [
    path('', AdView.as_view()),
    path('create/', NewAd.as_view()),
    path('<int:pk>/change/', UpdateAd.as_view()),
]