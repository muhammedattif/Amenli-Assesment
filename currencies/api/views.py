from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from currencies.serializers import CurrencyConversionSerializer
from djmoney.money import Money

class CurrencyConversionView(APIView):

    def get(self, request):
        params = self.request.query_params

        data = {
            'currency_in_currency': params.get('currency_in'),
            'currency_out_currency': params.get('currency_out'),
            'currency_in': params.get('currency_in_amount'),
            'currency_out': 0
        }
        serializer = CurrencyConversionSerializer(
                                                data=data,
                                                many=False,
                                                context={'user':request.user}
                                                )
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data)
