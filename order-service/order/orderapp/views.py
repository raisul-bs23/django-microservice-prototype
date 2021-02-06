from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK


class GetAllOrder(RetrieveAPIView):
    permission_classes = [AllowAny]

    def get(self, request):
        all_product_list = [
            {
                'id': 1,
                'name': 'Example order 1'
            },
            {
                'id': 2,
                'name': 'Example order 2'
            },

        ]
        return Response({
            'data': all_product_list,
            'message': 'Response From Order Service',
        }, status=HTTP_200_OK)