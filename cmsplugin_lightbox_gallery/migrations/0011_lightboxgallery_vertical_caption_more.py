# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_lightbox_gallery', '0010_lightboxgallery_rotating_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='lightboxgallery',
            name='vertical_caption_more',
            field=models.CharField(max_length=250, null=True, verbose_name='Vertical caption view more', blank=True),
        ),
    ]
