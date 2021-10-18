from rest_framework.views import APIView
from rest_framework.response import Response


class MyView(APIView):
    def get(self, *args, **kwargs):
        print(self.request.query_params)
        return Response({'msg': 'Hello from Get'})

    def post(self, *args, **kwargs):
        data = self.request.data
        print(data)
        return Response({'msg': 'Hello from Post'})

    def put(self, *args, **kwargs):
        return Response({'msg': 'Hello from Put'})

    def patch(self, *args, **kwargs):
        return Response({'msg': 'Hello from Patch'})

    def delete(self, *args, **kwargs):
        return Response({'msg': 'Hello from Delete'})
