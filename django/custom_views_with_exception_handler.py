from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status, viewsets, generics

class CustomAPIView(APIView):

    def handle_exception(self, exc):
        if isinstance(exc, ValidationError):
            data = {
                'status': False,
                'message': exc.detail if isinstance(exc.detail, list) else [exc.detail]
            }
            response = Response(data, status=status.HTTP_400_BAD_REQUEST)
            response.exception = True
            return response
        else:
            return super().handle_exception(exc)


class CustomViewSet(viewsets.ViewSet):

    def handle_exception(self, exc):
        if isinstance(exc, ValidationError):
            data = {
                'status': False,
                'message': exc.detail if isinstance(exc.detail, list) else [exc.detail]
            }
            response = Response(data, status=status.HTTP_400_BAD_REQUEST)
            response.exception = True
            return response
        else:
            return super().handle_exception(exc)


class CustomGenericView(generics.GenericAPIView):

    def handle_exception(self, exc):
        if isinstance(exc, ValidationError):
            data = {
                'status': False,
                'message': exc.detail if isinstance(exc.detail, list) else [exc.detail]
            }
            response = Response(data, status=status.HTTP_400_BAD_REQUEST)
            response.exception = True
            return response
        else:
            return super().handle_exception(exc)
