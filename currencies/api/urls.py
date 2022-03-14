from django.urls import path
from .views import CurrencyConversionView

app_name = 'currencies'

urlpatterns = [
    path('', CurrencyConversionView.as_view(), name='currency-conversion')
  ]
