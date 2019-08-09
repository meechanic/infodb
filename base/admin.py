# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from import_export import resources
from base.models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class SourceTagResource(resources.ModelResource):

    class Meta:
        model = SourceTag


class LinkTagResource(resources.ModelResource):

    class Meta:
        model = LinkTag


class SourceResource(resources.ModelResource):

    class Meta:
        model = Source


class LinkResource(resources.ModelResource):

    class Meta:
        model = Link


@admin.register(SourceTag)
class CategoryAdmin(ImportExportModelAdmin):
    resource_class = SourceTagResource


@admin.register(LinkTag)
class CategoryAdmin(ImportExportModelAdmin):
    resource_class = LinkTagResource


@admin.register(Source)
class CategoryAdmin(ImportExportModelAdmin):
    resource_class = SourceResource


@admin.register(Link)
class CategoryAdmin(ImportExportModelAdmin):
    resource_class = LinkResource
