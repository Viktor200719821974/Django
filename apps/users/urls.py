from django.urls import path

from .views import UsersListCreateView, UserRetrieveUpdateDestroyView, UserChangeIsActive, UserChangeIsStaff

urlpatterns = [
    path('', UsersListCreateView.as_view()),
    path('/<int:pk>', UserRetrieveUpdateDestroyView.as_view()),
    path('/<int:pk>/is_active/<int:bool>', UserChangeIsActive.as_view()),
    path('/<int:pk>/is_staff/<int:bool>', UserChangeIsStaff.as_view())

   ]