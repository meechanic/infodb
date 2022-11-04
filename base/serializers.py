from base.models import *
from rest_framework import serializers


class LinkTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinkTag
        fields = '__all__'


class SourceTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = SourceTag
        fields = '__all__'


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = '__all__'


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = '__all__'
