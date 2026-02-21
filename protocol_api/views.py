from django.contrib.auth.models import User
from django.http import Http404
from rest_framework import viewsets, mixins
from rest_framework.response import Response

from protocol_api.models import Protocol
from protocol_api.serializers import UserSerializer, ProtocolListSerializer, ProtocolDetailSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProtocolViewSet(mixins.CreateModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.ListModelMixin,
                      viewsets.GenericViewSet):
    queryset = Protocol.objects.defer('study_definition').all()
    lookup_field = 'name'

    def get_serializer_class(self):
        if self.action == 'list':
            return ProtocolListSerializer
        return ProtocolDetailSerializer

    def retrieve(self, request, *args, **kwargs):
        name = kwargs.get('name')
        protocol = Protocol.instances.get(name)
        if protocol is None:
            raise Http404
        serializer = self.get_serializer(protocol)
        return Response(serializer.data)
