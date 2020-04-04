# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse

# Create your models here.

class LinkTag(models.Model):
    name = models.TextField(unique = True)
    type = models.TextField()

    def __str__(self):
        return ' '.join([self.type, self.name])

    def __unicode__(self):
        return self.__str__()

    def get_absolute_url(self):
        return reverse('source-view', kwargs={'pk': self.id})

    class Meta:
        ordering = ['name']


class SourceTag(models.Model):
    name = models.TextField(unique = True)
    type = models.TextField()

    def __str__(self):
        return ' '.join([self.type, self.name])

    def __unicode__(self):
        return self.__str__()

    def get_absolute_url(self):
        return reverse('source-view', kwargs={'pk': self.id})

    class Meta:
        ordering = ['name']
        

class Link(models.Model):
    text = models.TextField()
    comment = models.TextField()
    scheme = models.TextField()
    base = models.TextField()
    path = models.TextField()
    edition = models.TextField()
    publisher = models.TextField()
    publishing_time = models.TextField()
    tag = models.ManyToManyField(LinkTag, blank=True)

    def __str__(self):
        return ' '.join([self.text, self.publisher, self.publishing_time])

    def __unicode__(self):
        return self.__str__()

    def get_absolute_url(self):
        return reverse('source-view', kwargs={'pk': self.id})

    class Meta:
        ordering = ['text']


class Source(models.Model):
    name = models.TextField(unique = True) # Any string, unique indentifies source
    clear_name = models.TextField() # Only name of source
    informal_name = models.TextField() # Any string, indentifies source, may be not unique
    comment = models.TextField()
    author_list = models.TextField()
    review = models.ManyToManyField('self', blank=True)
    tag = models.ManyToManyField(SourceTag, blank=True)
    link = models.ForeignKey(Link, blank=True, null=True, related_name='source_link', on_delete=models.CASCADE,)

    def __str__(self):
        return ' '.join([self.name])

    def __unicode__(self):
        return self.__str__()

    def get_absolute_url(self):
        return reverse('source-view', kwargs={'pk': self.id})

    class Meta:
        ordering = ['name']
