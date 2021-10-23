from django.urls import path

from .views import UsersListCreateView

urlpatterns = [
    path('', UsersListCreateView.as_view())

    ]