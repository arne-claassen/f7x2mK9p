from django.contrib.auth.models import User
from rest_framework import viewsets, mixins

from protocol_api.models import Protocol
from protocol_api.serializers import UserSerializer, ProtocolListSerializer, ProtocolDetailSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProtocolViewSet(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.ListModelMixin,
                      viewsets.GenericViewSet):
    queryset = Protocol.objects.all()
    lookup_field = 'name'

    def get_serializer_class(self):
        if self.action == 'list':
            return ProtocolListSerializer
        return ProtocolDetailSerializer
