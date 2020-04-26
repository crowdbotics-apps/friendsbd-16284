from rest_framework import authentication
from friendsBD.models import M1
from .serializers import M1Serializer
from rest_framework import viewsets


class M1ViewSet(viewsets.ModelViewSet):
    serializer_class = M1Serializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = M1.objects.all()
