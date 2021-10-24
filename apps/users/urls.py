from django.urls import path

from .views import UsersListCreateView, UserRetrieveUpdateDestroyView, UserChangeIsActionFalseView, UserChangeIsActionTrueView, UserChangeIsStaffFalseView, UserChangeIsStaffTrueView

urlpatterns = [
    path('', UsersListCreateView.as_view()),
    path('/<int:pk>', UserRetrieveUpdateDestroyView.as_view()),
    path('/<int:pk>/is_action_false', UserChangeIsActionFalseView.as_view()),
    path('/<int:pk>/is_action_true', UserChangeIsActionTrueView.as_view()),
    path('/<int:pk>/is_staff_false', UserChangeIsStaffFalseView.as_view()),
    path('/<int:pk>/is_staff_true', UserChangeIsStaffTrueView.as_view())
   ]