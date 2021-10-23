from rest_framework.generics import ListCreateAPIView
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from .serializers import UserModelSerializer

UserModel: User = get_user_model()

class UsersListCreateView(ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer