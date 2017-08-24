# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0006_auto_20160623_1627'),
        ('cmsplugin_lightbox_gallery', '0012_auto_20160815_0939'),
    ]

    operations = [
        migrations.AddField(
            model_name='lightboxgalleryimage',
            name='crop',
            field=models.BooleanField(default=True, verbose_name='crop'),
        ),
        migrations.AddField(
            model_name='lightboxgalleryimage',
            name='height',
            field=models.PositiveIntegerField(null=True, verbose_name='height', blank=True),
        ),
        migrations.AddField(
            model_name='lightboxgalleryimage',
            name='thumbnail_option',
            field=models.ForeignKey(blank=True, to='filer.ThumbnailOption', help_text='overrides width, height, crop and upscale with values from the selected thumbnail option', null=True, verbose_name='thumbnail option'),
        ),
        migrations.AddField(
            model_name='lightboxgalleryimage',
            name='upscale',
            field=models.BooleanField(default=True, verbose_name='upscale'),
        ),
        migrations.AddField(
            model_name='lightboxgalleryimage',
            name='use_autoscale',
            field=models.BooleanField(default=False, help_text='tries to auto scale the image based on the placeholder context', verbose_name='use automatic scaling'),
        ),
        migrations.AddField(
            model_name='lightboxgalleryimage',
            name='use_original_image',
            field=models.BooleanField(default=False, help_text='do not resize the image. use the original image instead.', verbose_name='use the original image'),
        ),
        migrations.AddField(
            model_name='lightboxgalleryimage',
            name='width',
            field=models.PositiveIntegerField(null=True, verbose_name='width', blank=True),
        ),
    ]
