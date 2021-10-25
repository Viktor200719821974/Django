from typing import Union, Tuple, Any

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


# class UserChangeIsActionFalseView(RetrieveUpdateDestroyAPIView):
#     queryset = UserModel.objects.all()
#     serializer_class = UserModelSerializer
#
#     def patch(self, request, *args, **kwargs):
#         pk = kwargs.get('pk')
#         user = UserModel.objects.filter(pk=pk).update(is_active=False)
#         return user


class UserChangeIsActiveTrueView(GenericAPIView):
    queryset = UserModel.objects.all()

    def patch(self, *args, **kwargs):

        user = self.get_object()
        user.is_active = True
        user.save()
        serializer = UserModelSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)

#
# class UserChangeIsActiveFalseView(GenericAPIView):
#     queryset = UserModel.objects.all()
#
#     def patch(self, request, bool):
#         user = self.get_object()
#         user.is_active = False
#         user.save()
#         serializer = UserModelSerializer(user)
#         return Response(serializer.data, status.HTTP_200_OK)
# 

# class UserToAdminTrueView(GenericAPIView):
# #     queryset = UserModel.objects.all()
# #
# #     def patch(self, *args, **kwargs):
# #         user = self.get_object()
# #         user.is_staff = True
# #         user.save()
# #         serializer = UserModelSerializer(user)
# #         return Response(serializer.data, status.HTTP_200_OK)
# #
# #
# # class UserToAdminFalseView(GenericAPIView):
# #     queryset = UserModel.objects.all()
# #
# #     def patch(self, *args, **kwargs):
# #         user = self.get_object()
# #         user.is_active = False
# #         user.save()
# #         serializer = UserModelSerializer(user)
# #         return Response(serializer.data, status.HTTP_200_OK)
