from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins, status
from rest_framework.generics import (GenericAPIView, ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView,
                                     get_object_or_404)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.utils.decorators import method_decorator

from .models import CarModel
from .serializer import CarModelSerializer
from .filters import CarFilter


###############################################################

# # Generic  (ListCreateAPIView,RetrieveUpdateDestroyAPIView)
@method_decorator(name='get', decorator=swagger_auto_schema(operation_id='List of car', operation_summary='Get all'))
class CarListCreateView(ListCreateAPIView):
    """
    get:
        Get all cars
    post:
        Create car
    """

    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer
    permission_classes = (AllowAny,)
    # filterset_fields = ('year', 'brand', 'model', 'color')
    filterset_class = CarFilter


# Filter
#     def get_queryset(self):
#         auto_park_id = self.request.query_params.get('autoParkId')
#         qs = CarModel.objects.all()
#         if auto_park_id:
#             qs = qs.filter(autoPark_id=auto_park_id)
#         return qs

class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer

###########################################################

# mixins

# class CarListCreateView(GenericAPIView,mixins.CreateModelMixin,mixins.ListModelMixin):
#     queryset = CarModel.objects.all()
#     serializer_class = CarModelSerializer

# def get(self, request, *args, **kwargs):
#     return super().list(request, *args, **kwargs)

# def post(self, request, *args, **kwargs):
#     return super().create(request, *args, **kwargs)
#
# class CarRetrieveUpdateDestroyView(GenericAPIView,mixins.RetrieveModelMixin, mixins.DestroyModelMixin,
# mixins.UpdateModelMixin):
#     queryset = CarModel.objects.all()
#     serializer_class = CarModelSerializer

#     def get(self, request, *args, **kwargs):
#         return super().retrieve(request, *args, **kwargs)
#
#     def patch(self, request, *args, **kwargs):
#         return super().update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return super().destroy(request, *args, **kwargs)

###########################################################

# ApiView
# class CarListCreateView(APIView):
#     def get(self, *args, **kwargs):
#       cars = CarModel.objects.all()
#       serializer = CarModelSerializer(cars, many=True)
#       return Response(serializer.data, status.HTTP_200_OK)
#
#     def post(self, *args, **kwargs):
#        data = self.request.data
#        serializer = CarModelSerializer(data=data)
#        serializer.is_valid(raise_exception=True)
#        serializer.save()
#        return Response(serializer.data, status.HTTP_201_CREATED)
#
#
# class CarRetrieveUpdateDestroyView(GenericAPIView):
#
#     def get(self, *args, **kwargs):
#         car = self.get_object()
#         serializer = CarModelSerializer(car)
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def put(self, *args, **kwargs):
#         pk = kwargs.get('pk')
#         data = self.request.data
#         car = get_object_or_404(CarModel, pk=pk)
#         serializer = CarModelSerializer(car, data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def patch(self, *args, **kwargs):
#         data = self.request.data
#         car = self.get_object()
#         serializer = CarModelSerializer(car, data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def delete(self, *args, **kwargs):
#         car = self.get_object()
#         car.delete()
#         return Response('Car deleted', status.HTTP_204_NO_CONTENT)
