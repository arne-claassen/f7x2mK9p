from django.contrib.auth.models import User
from rest_framework import serializers

from protocol_api.models import Protocol


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class ProtocolListSerializer(serializers.HyperlinkedModelSerializer):

    study_reference = serializers.SerializerMethodField()

    def get_study_reference(self, obj):
        return obj.study.reference

    class Meta:
        model = Protocol
        fields = ['url', 'name', 'study_reference', 'created_at']
        extra_kwargs = {
            'url': {'lookup_field': 'name'}
        }


class ProtocolDetailSerializer(serializers.HyperlinkedModelSerializer):

    study_reference = serializers.SerializerMethodField()

    def get_study_reference(self, obj):
        return obj.study.reference

    class Meta:
        model = Protocol
        fields = ['url', 'name', 'created_at', 'study_definition', 'study_reference']
        extra_kwargs = {
            'url': {'lookup_field': 'name'}
        }
