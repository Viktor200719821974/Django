from django.urls import path

from auto_park.views import AutoParkRetrieveUpdateDestroyView
from .views import CarListCreateView, CarRetrieveUpdateDestroyView

urlpatterns = [
    path('', CarListCreateView.as_view()),
    path('/<int:pk>', CarRetrieveUpdateDestroyView.as_view()),
path('/<int:pk>', AutoParkRetrieveUpdateDestroyView.as_view())

]