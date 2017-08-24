# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_lightbox_gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lightboxgallery',
            name='has_preview',
            field=models.BooleanField(default=False, verbose_name='Gallery has preview'),
        ),
        migrations.AddField(
            model_name='lightboxgallery',
            name='name',
            field=models.CharField(max_length=250, null=True, verbose_name='Gallery name', blank=True),
        ),
        migrations.AddField(
            model_name='lightboxgallery',
            name='preview_amount',
            field=models.IntegerField(default=0, null=True, verbose_name='Amount of images for preview', blank=True),
        ),
        migrations.AlterField(
            model_name='lightboxgallery',
            name='button_classes',
            field=models.CharField(max_length=250, null=True, verbose_name='Launch gallery button classes', blank=True),
        ),
        migrations.AlterField(
            model_name='lightboxvideo',
            name='button_classes',
            field=models.CharField(max_length=250, null=True, verbose_name='Watch video button classes', blank=True),
        ),
    ]
