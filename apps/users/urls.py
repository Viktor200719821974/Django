from django.urls import path

from .views import UsersListCreateView, UserRetrieveUpdateDestroyView, UserChangeIsActiveTrueView
# , UserChangeIsStaffTrueView, UserChangeIsStaffFalseView

urlpatterns = [
    path('', UsersListCreateView.as_view()),
    path('/<int:pk>', UserRetrieveUpdateDestroyView.as_view()),
    path('/<int:pk>/is_active/true', UserChangeIsActiveTrueView.as_view()),

    # path('/<int:pk>/is_staff/true', UserChangeIsStaffTrueView.as_view()),
    # path('/<int:pk>/is_staff/false', UserChangeIsStaffFalseView.as_view())
   ]