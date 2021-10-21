from rest_framework.serializers import ModelSerializer

from .models import CarModel

class CarModelSerializer(ModelSerializer):

    class Meta:
        model = CarModel
        fields = '__all__'
        extra_kwargs = {
            'autoPark':{'read_only':True},
        }
