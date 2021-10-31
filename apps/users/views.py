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

    def get_queryset(self):
        return UserModel.objects.exclude(id=self.request.user.id)

    def get_serializer_context(self):
        return {'request':self.request}


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
        if bool not in [1,0]:
            return Response('Value must be 0 and 1', status.HTTP_400_BAD_REQUEST)
        user = self.get_object()
        user.is_staff = bool
        user.save()
        serializer = UserModelSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class UserToSuperAdminView(GenericAPIView):
    permission_classes = (IsSuperUser,)
    queryset = UserModel.objects.all()

    def patch(self, *args, **kwargs):
        user = self.get_object()
        UserModel.objects.to_superadmin(user)
        # user.is_superuser = True
        user.save()
        data = UserModelSerializer(user).data
        return Response(data, status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        user = self.get_object()
        UserModel.objects.to_user(user)
        # user.is_superuser =False
        user.save()
        data = UserModelSerializer(user).data
        return Response(data, status.HTTP_200_OK)


class AvatarView(GenericAPIView):

    def patch(self, *args, **kwargs):
        avatar_data = self.request.FILES.get('avatar')
        serializer = AvatarSerializer(data={'url': avatar_data})
        serializer.is_valid(raise_exception=True)
        serializer.save(profile=self.request.user.profile)
        user = UserModelSerializer(self.request.user).data
        return Response(user, status.HTTP_200_OK)
