from django.contrib import admin
from import_export import resources
from base.models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class InfsourceResource(resources.ModelResource):

    class Meta:
        model = Infsource


class EditionResource(resources.ModelResource):

    class Meta:
        model = Edition


class ResourceResource(resources.ModelResource):

    class Meta:
        model = Resource


@admin.register(Infsource)
class CategoryAdmin(ImportExportModelAdmin):
    resource_class = InfsourceResource


@admin.register(Edition)
class CategoryAdmin(ImportExportModelAdmin):
    resource_class = EditionResource


@admin.register(Resource)
class CategoryAdmin(ImportExportModelAdmin):
    resource_class = ResourceResource
