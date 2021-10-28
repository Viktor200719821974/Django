from django.contrib.auth import get_user_model

from apps.profile.serializers import ProfileModelSerializer
from rest_framework.serializers import ModelSerializer

from django4.utils.jwt_utils import JwtUtils
from .models import UserModel as User
from apps.profile.models import ProfileModel
from django4.utils.email_utils import EmailUtils

UserModel: User = get_user_model()


class UserModelSerializer(ModelSerializer):
    profile = ProfileModelSerializer()

    class Meta:
        model = UserModel
        fields = (
            'id', 'email', 'password', 'is_active', 'is_staff', 'is_superuser', 'last_login', 'created_at',
            'updated_at', 'profile'
        )
        extra_kwargs = {
            'password': {'write_only': True}

        }

    def create(self, validated_data: dict):
        profile = validated_data.pop('profile')
        user = UserModel.objects.create_user(**validated_data)
        ProfileModel.objects.create(**profile, user=user)
        token = JwtUtils('activate', {'minutes': 30}).create_token(user)
        request = self.context.get('request')
        EmailUtils.register_email(user.email, profile.get('name'), token, request)
        return user
