from rest_framework import serializers

from network import models


class NetworkSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Network
        fields = ("id", "title", "arrears")
