from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from rest_framework import serializers
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

User = get_user_model()


"""
It is a Model serializer so the customization on the model Fields validators doesn't take effect.

"""


class UserSerializer(serializers.ModelSerializer):


    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'first_name', 'last_name', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, user):
        if user['password'] != self.context['password2']:
            raise serializers.ValidationError({'password':'Password does not match.'})
        return user

class AuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if not (email or password):
            msg = 'Must include "email" and "password"'
            raise serializers.ValidationError({
                'status': 'error',
                'message': msg
            })

        user = authenticate(email=email, password=password)

        if not user:
            msg = 'Unable to log in with provided credentials.'
            raise serializers.ValidationError({
                'status': 'error',
                'message': msg
            })

        if not user.is_active:
            msg = 'User account is disabled.'
            raise serializers.ValidationError({
                'status': 'error',
                'message': msg
            })


        attrs['user'] = user
        return attrs
