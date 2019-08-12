# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from base.models import *
from base.serializers import *
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

# Create your views here.

@api_view(['GET'])
@authentication_classes((SessionAuthentication, BasicAuthentication, TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def api_root(request, format=None):
    """
    The entry endpoint of our API.
    """
    return Response({
        'linktags': reverse('api-linktag', request=request),
        'sourcetags': reverse('api-sourcetag', request=request),
        'links': reverse('api-link', request=request),
        'sources': reverse('api-source', request=request),
    })


@authentication_classes((SessionAuthentication, BasicAuthentication, TokenAuthentication,))
@permission_classes((IsAuthenticated,))
class ApiLinkTag(viewsets.ModelViewSet):
    """
    API endpoint that represents a list of objects.
    """
    queryset = LinkTag.objects.all()
    serializer_class = LinkTagSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields=('name',)
    search_fields=('name',)


@authentication_classes((SessionAuthentication, BasicAuthentication, TokenAuthentication,))
@permission_classes((IsAuthenticated,))
class ApiSourceTag(viewsets.ModelViewSet):
    """
    API endpoint that represents a list of objects.
    """
    queryset = SourceTag.objects.all()
    serializer_class = SourceTagSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields=('name',)
    search_fields=('name',)


@authentication_classes((SessionAuthentication, BasicAuthentication, TokenAuthentication,))
@permission_classes((IsAuthenticated,))
class ApiLink(viewsets.ModelViewSet):
    """
    API endpoint that represents a list of objects.
    """
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields=('text',)
    search_fields=('text',)


@authentication_classes((SessionAuthentication, BasicAuthentication, TokenAuthentication,))
@permission_classes((IsAuthenticated,))
class ApiSource(viewsets.ModelViewSet):
    """
    API endpoint that represents a list of objects.
    """
    queryset = Source.objects.all()
    serializer_class = SourceSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields=('name',)
    search_fields=('name',)
