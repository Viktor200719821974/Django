from rest_framework.serializers import ModelSerializer

from .models import AutoParkModel
from cars.serializer import CarModelSerializer


class AutoParkmodelSerializer(ModelSerializer):
    cars = CarModelSerializer(many=True)

    class Meta:
        model = AutoParkModel
        fields = '__all__'

    def create(self, validated_data):
        return super().create(validated_data)
