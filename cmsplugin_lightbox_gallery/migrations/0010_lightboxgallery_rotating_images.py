# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_lightbox_gallery', '0009_auto_20160729_0755'),
    ]

    operations = [
        migrations.AddField(
            model_name='lightboxgallery',
            name='rotating_images',
            field=models.IntegerField(default=0, null=True, verbose_name='Amount of images for rotating banner', blank=True),
        ),
    ]
