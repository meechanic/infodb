from base.models import *
from rest_framework import serializers


class InfsourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Infsource
        fields = '__all__'


class InfsourceTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfsourceTag
        fields = '__all__'


class EditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Edition
        fields = '__all__'


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = '__all__'
