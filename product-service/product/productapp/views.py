from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response


class GetAllProducts(RetrieveAPIView):
    permission_classes = [AllowAny]

    def get(self, request):
        all_product_list = [
            {
                'id': 1,
                'name': 'Example product 1'
            },
            {
                'id': 2,
                'name': 'Example product 2'
            },

        ]
        return Response({
            'data': all_product_list,
            'message': 'Response From Product Service',
        }, status=HTTP_200_OK)