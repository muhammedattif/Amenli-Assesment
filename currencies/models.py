from django.db import models
from model_utils import Choices
from .settings import SUPPORTED_CURRENCIES
from django.contrib.auth import get_user_model
from djmoney.models.fields import MoneyField
from djmoney.models.validators import MaxMoneyValidator, MinMoneyValidator

User = get_user_model()

class CurrencyPair(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='conversions')

    currency_in = MoneyField(max_digits=14, decimal_places=4, default=1,
        validators=[
        MinMoneyValidator(1)
        ], default_currency='USD')

    currency_out = MoneyField(max_digits=14, decimal_places=4, default=0,
        validators=[
        MinMoneyValidator(0)
        ], default_currency='EGP')

    class Meta:
        verbose_name_plural = 'Currency Pairs'

    def __str__(self):
        return f'{self.user.username}-{self.currency_in.currency}->{self.currency_out.currency}'
