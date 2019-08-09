from base.models import *
from rest_framework import serializers


class LinkTagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LinkTag
        fields = '__all__'


class SourceTagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SourceTag
        fields = '__all__'


class LinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Link
        fields = '__all__'


class SourceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Source
        fields = '__all__'
