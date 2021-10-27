from rest_framework.serializers import ModelSerializer

from .models import ProfileModel, AvatarModel



class AvatarSerializer(ModelSerializer):
    class Meta:
        model = AvatarModel
        fields = ('url',)


class ProfileModelSerializer(ModelSerializer):
    avatars = AvatarSerializer(many=True, read_only=True)

    class Meta:
        model = ProfileModel
        exclude = ('user',)
