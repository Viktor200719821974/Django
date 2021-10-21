from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView,GenericAPIView, get_object_or_404
from rest_framework import mixins

from .models import CarModel
from .serializer import CarModelSerializer
###############################################################

# # Generic  (ListCreateAPIView,RetrieveUpdateDestroyAPIView)

class CarListCreateView(ListCreateAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer
########################################################################
    # FILTER

    # def get_queryset(self):
    #     year = self.request.query_params.get('year')
    #     qs = CarModel.objects.all()
    #     if year:
    #         qs = qs.filter(year__gte=year)
    #     return qs
#########################################################################

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
# class CarRetrieveUpdateDestroyView(GenericAPIView,mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin):
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

    # def get(self, *args, **kwargs):
    #     cars = CarModel.objects.all()
    #     serializer = CarModelSerializer(cars, many=True)
    #     return Response(serializer.data, status.HTTP_200_OK)
    #
    # def post(self, *args, **kwargs):
    #     data = self.request.data
    #     serializer = CarModelSerializer(data=data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status.HTTP_201_CREATED)


# class CarRetrieveUpdateDestroyView(GenericAPIView):
#     queryset = CarModel.objects.all()
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
