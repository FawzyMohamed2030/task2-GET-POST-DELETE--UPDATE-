from rest_framework import serializers
from . import models


class Caractersserializer(serializers.ModelSerializer):
    class Meta:
        model = models.Characters
        fields = '__all__'