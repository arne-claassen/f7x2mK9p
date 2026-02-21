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
        fields = ['url', 'name',  'description', 'study_reference', 'created_at']
        extra_kwargs = {
            'url': {'lookup_field': 'name'}
        }


class ProtocolDetailSerializer(serializers.HyperlinkedModelSerializer):
    UPDATABLE_FIELDS = {'description', 'study_definition'}

    study_reference = serializers.SerializerMethodField()

    def get_study_reference(self, obj):
        return obj.study.reference

    class Meta:
        model = Protocol
        fields = ['url', 'name', 'created_at', 'description', 'study_definition', 'study_reference']
        extra_kwargs = {
            'url': {'lookup_field': 'name'}
        }

    def get_extra_kwargs(self):
        extra_kwargs = super().get_extra_kwargs()

        if self.instance is not None:
            read_only_fields = set(self.Meta.fields) - self.UPDATABLE_FIELDS
            for field_name in read_only_fields:
                extra_kwargs.setdefault(field_name, {})['read_only'] = True

        return extra_kwargs
