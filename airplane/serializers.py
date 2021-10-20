from rest_framework.serializers import ModelSerializer

from .models import AirPlaneModel


class AirPlaneSerializer(ModelSerializer):
    class Meta:
        model = AirPlaneModel
        fields = '__all__'
