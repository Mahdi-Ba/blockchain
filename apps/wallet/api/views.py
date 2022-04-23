import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.wallet.api.serializer import AddressInfoSerializer
from apps.wallet.api.service import WalletService


class AddressInfo(APIView, WalletService):
    def post(self, request):
        serializer = AddressInfoSerializer(data=request.data)
        if serializer.is_valid():
            return Response({
                'success': True,
                'message': "Address Information",
                'dev_message': "Address Information",
                'data': self.getAddressInfo(request)
            },
                status=status.HTTP_200_OK)
        return Response(
            {'success': False,
             'message': 'warning!! error occurred',
             'data': {'messages': serializer.errors}},
            status.HTTP_400_BAD_REQUEST)
