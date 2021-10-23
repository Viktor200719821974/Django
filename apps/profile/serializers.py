from rest_framework.serializers import ModelSerializer
from .models import ProfileModel

class ProfileModelSerializer(ModelSerializer):
    class Meta:
        model = ProfileModel
        # fields = '__all__'
        exclude = ('user',)