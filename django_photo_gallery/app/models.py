#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import uuid
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit

class Album(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField(max_length=510)
    thumb = ProcessedImageField(upload_to='albums', processors=[ResizeToFit(500)], format='JPEG', options={'quality': 90})
    tags = models.CharField(max_length=250)
    is_visible = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=60, unique=True)

    #def get_absolute_url(self):
    #    return reverse('album', kwargs={'slug':self.slug})

    def __unicode__(self):
        return self.title

class AlbumImage(models.Model):
    image = ProcessedImageField(upload_to='albums', processors=[ResizeToFit(1280)], format='JPEG', options={'quality': 60})
    thumb = ProcessedImageField(upload_to='albums', processors=[ResizeToFit(500)], format='JPEG', options={'quality': 70})
    album = models.ForeignKey('album', on_delete=models.PROTECT)
    alt = models.CharField(max_length=255, default=uuid.uuid4)
    created = models.DateTimeField(auto_now_add=True)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    slug = models.SlugField(max_length=71, default=uuid.uuid4, editable=False)