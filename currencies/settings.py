from django.conf import settings

SUPPORTED_CURRENCIES = getattr(settings, 'CURRENCIES', ('EGP', 'EUR', 'USD') )
