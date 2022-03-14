from django.urls import path
from .views import UserCreateView, AuthToken
app_name = 'users'

urlpatterns = [
    path('', UserCreateView.as_view(), name='user-create'),
    path('auth-token', AuthToken.as_view(), name='auth-token')
]
