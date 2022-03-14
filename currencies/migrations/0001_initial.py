# Generated by Django 4.0.3 on 2022-03-14 08:52

from decimal import Decimal
from django.db import migrations, models
import djmoney.models.fields
import djmoney.models.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CurrencyPair',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency_in_currency', djmoney.models.fields.CurrencyField(choices=[('EGP', 'EGP L.E'), ('EUR', 'EUR €'), ('USD', 'USD $')], default='USD', editable=False, max_length=3)),
                ('currency_in', djmoney.models.fields.MoneyField(decimal_places=4, default=Decimal('1'), default_currency='USD', max_digits=14, validators=[djmoney.models.validators.MinMoneyValidator(1)])),
                ('currency_out_currency', djmoney.models.fields.CurrencyField(choices=[('EGP', 'EGP L.E'), ('EUR', 'EUR €'), ('USD', 'USD $')], default='EGP', editable=False, max_length=3)),
                ('currency_out', djmoney.models.fields.MoneyField(decimal_places=4, default=Decimal('0'), default_currency='EGP', max_digits=14, validators=[djmoney.models.validators.MinMoneyValidator(0)])),
            ],
            options={
                'verbose_name_plural': 'Currency Pairs',
            },
        ),
    ]