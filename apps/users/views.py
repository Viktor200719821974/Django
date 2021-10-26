from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .serializers import UserModelSerializer

UserModel: User = get_user_model()


class UsersListCreateView(ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer
    permission_classes = (AllowAny,)


class UserRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer


class UserChangeIsActive(GenericAPIView):
    queryset = UserModel.objects.all()

    def patch(self, *args, **kwargs):
        bool = kwargs.get('bool')
        user = self.get_object()
        user.is_active = bool
        user.save()
        serializer = UserModelSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class UserChangeIsStaff(GenericAPIView):
    queryset = UserModel.objects.all()

    def patch(self, *args, **kwargs):
        bool = kwargs.get('bool')
        user = self.get_object()
        user.is_staff = bool
        user.save()
        serializer = UserModelSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)

