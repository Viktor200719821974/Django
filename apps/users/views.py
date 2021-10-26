from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView, UpdateAPIView
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .serializers import UserModelSerializer
from .permissions import IsSuperUser
from apps.profile.serializers import AvatarSerializer

UserModel: User = get_user_model()


class UsersListCreateView(ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return AllowAny(),
        return IsAuthenticated(),


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


class UserToAdminView(GenericAPIView):
    permission_classes = (IsSuperUser,)
    queryset = UserModel.objects.all()

    def path(self, *args, **kwargs):
        user = self.get_object()
        user.is_superuser = True
        user.save()
        data = UserModelSerializer(user).data
        return Response(data, status.HTTP_200_OK)


class AvatarView(UpdateAPIView):
    serializer_class = AvatarSerializer

    def get_object(self):
        return self.request.user.profile
