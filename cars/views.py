from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import CarModel
from .serializer import CarModelSerializer


class CarListCreateView(APIView):
    def get(self, *args, **kwargs):
        cars = CarModel.objects.all()
        serializer = CarModelSerializer(cars, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = CarModelSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class CarRetrieveUpdateDestroyView(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        exists = CarModel.objects.filter(pk=pk).exists()
        if not exists:
            return Response('Not found', status.HTTP_404_NOT_FOUND)
        car = CarModel.objects.get(pk=pk)
        serializer = CarModelSerializer(car)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        pk = kwargs.get('pk')
        data = self.request.data
        exists = CarModel.objects.filter(pk=pk).exists()
        if not exists:
            return Response('Not found', status.HTTP_404_NOT_FOUND)
        car = CarModel.objects.get(pk=pk)
        serializer = CarModelSerializer(car, data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, *args, **kwargs):
        pk = kwargs.get('pk')
        data = self.request.data
        exists = CarModel.objects.filter(pk=pk).exists()
        if not exists:
            return Response('Not found', status.HTTP_404_NOT_FOUND)
        car = CarModel.objects.get(pk=pk)
        serializer = CarModelSerializer(car, data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')
        exists = CarModel.objects.filter(pk=pk).exists()
        if not exists:
            return Response('Not found', status.HTTP_404_NOT_FOUND)
        car = CarModel.objects.get(pk=pk)
        car.delete()
        return Response('Car deleted', status.HTTP_204_NO_CONTENT)
