from django.contrib.auth.models import User
from rest_framework import serializers

from protocol_api.models import Protocol


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class ProtocolSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Protocol
        fields = ['url', 'name', 'created_at']
        extra_kwargs = {
            'url': {'lookup_field': 'name'}
        }