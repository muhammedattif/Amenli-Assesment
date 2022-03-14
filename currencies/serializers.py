from rest_framework import serializers
from .models import CurrencyPair
from google_currency import convert
from djmoney.money import Money
from users.serializers import UserSerializer
import json
from .settings import SUPPORTED_CURRENCIES

class CurrencyConversionSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    class Meta:
        model = CurrencyPair
        fields = '__all__'


    def validate(self, object):
        if object['currency_in'].currency == object['currency_out'].currency:
            raise serializers.ValidationError({'error':'Currency pairs cannot be the same.'})

        if str(object['currency_in'].currency) not in SUPPORTED_CURRENCIES:
            raise serializers.ValidationError({'error':f"{object['currency_in'].currency} is not supported."})

        if str(object['currency_out'].currency) not in SUPPORTED_CURRENCIES:
            raise serializers.ValidationError({'error':f"{object['currency_out'].currency} is not supported."})
        return object


    def create(self, validated_data):
        user = self.context.get('user')
        validated_data['user'] = user

        # Here we can use Djmoney conversion rates but it seems that it does not support EGP
        # So, user google currency instead
        converted_currency_out = json.loads(convert(
                                                str(validated_data['currency_in'].currency),
                                                str(validated_data['currency_out'].currency),
                                                float(validated_data['currency_in'].amount)
                                                )
                                            )

        validated_data['currency_out'].amount = converted_currency_out['amount']
        currency_pairs = CurrencyPair.objects.create(**validated_data)
        return currency_pairs
