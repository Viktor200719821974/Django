from rest_framework.serializers import ModelSerializer

from apps.cars.serializer import CarModelSerializer

from .models import AutoParkModel


class AutoParkmodelSerializer(ModelSerializer):
    cars = CarModelSerializer(many=True)

    class Meta:
        model = AutoParkModel
        fields = '__all__'

    def create(self, validated_data):
        return super().create(validated_data)
