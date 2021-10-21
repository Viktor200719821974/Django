from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import AutoParkModel
from .serializer import AutoParkmodelSerializer


class AutoParkListCreateView(APIView):
    def get(self, *args, **kwargs):
        autoparks = AutoParkModel.objects.get()
        serializer = AutoParkmodelSerializer(autoparks, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = AutoParkmodelSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class AutoParkRetrieveUpdateDestroyView(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        exists = AutoParkModel.objects.filter(pk=pk).exists()
        if not exists:
            return Response('Not found', status.HTTP_404_NOT_FOUND)
        autopark = AutoParkModel.objects.get(pk=pk)
        serializer = AutoParkmodelSerializer(autopark)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        pk = kwargs.get('pk')
        data = self.request.data
        exists = AutoParkModel.objects.filter(pk=pk).exists()
        if not exists:
            return Response('Not found', status.HTTP_404_NOT_FOUND)
        autopark = AutoParkModel.objects.get()
        serializer = AutoParkmodelSerializer(autopark, data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, *args, **kwargs):
        pk = kwargs.get('pk')
        data = self.request.data
        exists = AutoParkModel.objects.filter(pk=pk).exists()
        if not exists:
            return Response('Not found', status.HTTP_404_NOT_FOUND)
        autopark = AutoParkModel.objects.get(pk=pk)
        serializer = AutoParkmodelSerializer(autopark, data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')
        exists = AutoParkModel.objects.filter(pk=pk).exists()
        if not exists:
            return Response('Not found', status.HTTP_404_NOT_FOUND)
        autopark = AutoParkModel.objects.get(pk=pk)
        autopark.delete()
        return Response('AutoPark deleted', status.HTTP_204_NO_CONTENT)
