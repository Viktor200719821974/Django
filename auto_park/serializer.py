from rest_framework.serializers import ModelSerializer

from .models import AutoParkModel

class AutoParkmodelSerializer(ModelSerializer):
    class Meta:
        model= AutoParkModel
        fields= '__all__'