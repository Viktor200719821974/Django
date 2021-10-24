from typing import Union, Tuple, Any

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny

from .serializers import UserModelSerializer

UserModel: User = get_user_model()


class UsersListCreateView(ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer
    permission_classes = (AllowAny,)


class UserRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer

class UserChangeIsActionFalseView(RetrieveUpdateDestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer

    def patch(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        user = UserModel.objects.filter(pk=pk).update(is_active = False)
        return user

class UserChangeIsActionTrueView(RetrieveUpdateDestroyAPIView):

    def patch(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        user = UserModel.objects.filter(pk=pk).update(is_active=True)
        return user

class UserChangeIsStaffFalseView(RetrieveUpdateDestroyAPIView):
    def patch(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        user = UserModel.objects.filter(pk=pk).update(is_staff=False)
        return user
    
class UserChangeIsStaffTrueView(RetrieveUpdateDestroyAPIView):
    def patch(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        user = UserModel.objects.filter(pk=pk).update(is_staff=True)
        return user