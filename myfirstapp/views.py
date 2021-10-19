from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .utils import DBUtils


class ComputerListCreateView(APIView):
    def get(self, *args, **kwargs):
        computers = DBUtils.read_db()
        return Response(computers, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        computer = self.request.data
        created_computer = DBUtils.create(computer)
        return Response(created_computer, status.HTTP_201_CREATED)


class ComputerRetrieveUpdateDestroyView(APIView):

    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        computers = DBUtils.read_db()
        for computer in computers:
            if computer.get('id') == pk:
                return Response(computer, status.HTTP_200_OK)
        return Response('Computer with this id is not found', status.HTTP_404_NOT_FOUND)

    def patch(self, *args, **kwargs):
        pk = kwargs.get('pk')
        data = self.request.data
        computers = DBUtils.read_db()
        computer = DBUtils.update(data, pk)
        if not computer:
            return Response('Computer with this id is not found', status.HTTP_404_NOT_FOUND)
        return Response(computer, status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')
        is_delete = DBUtils.delete(pk)
        if not is_delete:
            return Response('Computer with this id is not found', status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)