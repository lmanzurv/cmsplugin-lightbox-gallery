# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import aldryn_bootstrap3.model_fields


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_lightbox_gallery', '0011_lightboxgallery_vertical_caption_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lightboxgallery',
            name='button_icon_left',
            field=aldryn_bootstrap3.model_fields.Icon(default='', max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='lightboxgallery',
            name='button_icon_right',
            field=aldryn_bootstrap3.model_fields.Icon(default='', max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='lightboxgallery',
            name='button_text',
            field=models.CharField(max_length=250, null=True, verbose_name='Launch gallery button label', blank=True),
        ),
    ]
