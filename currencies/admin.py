from django.contrib import admin
from .models import CurrencyPair


class CurrencyPairConfig(admin.ModelAdmin):

    model = CurrencyPair

    list_filter = (
    'user',
    'currency_in_currency',
    'currency_out_currency',
    )

    list_display = (
    'user',
    'currency_in',
    'currency_out'
    )

    search_fields = ('user', 'currency_in__currency', 'currency_out__currency')
    readonly_fields = ('user', 'currency_in', 'currency_out')
    
    # To avoid hitting the DB
    list_select_related = ('user', )


admin.site.register(CurrencyPair, CurrencyPairConfig)
