from rest_framework import serializers
from friendsBD.models import M1


class M1Serializer(serializers.ModelSerializer):
    class Meta:
        model = M1
        fields = "__all__"
