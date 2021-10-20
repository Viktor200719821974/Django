from django.urls import path

from .views import AirPlaneListCreateView, AirPlaneRetrieveUpdateDestroyView

urlpatterns = [
    path('', AirPlaneListCreateView.as_view()),
    path('/<int:pk>', AirPlaneRetrieveUpdateDestroyView.as_view())
]