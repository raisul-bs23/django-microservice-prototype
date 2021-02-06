from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK


class GetAllInvoice(RetrieveAPIView):
    permission_classes = [AllowAny]

    def get(self, request):
        all_product_list = [
            {
                'id': 1,
                'name': 'Example Invoice 1'
            },
            {
                'id': 2,
                'name': 'Example Invoice 2'
            },

        ]
        return Response({
            'data': all_product_list,
            'message': 'Response From Invoice Service',
        }, status=HTTP_200_OK)