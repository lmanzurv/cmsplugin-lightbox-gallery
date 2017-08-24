# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_urlconfrevision'),
        ('cmsplugin_lightbox_gallery', '0004_auto_20160606_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='lightboxgallery',
            name='vertical_caption',
            field=models.BooleanField(default=False, verbose_name='Vertical caption'),
        ),
        migrations.AddField(
            model_name='lightboxgalleryoverview',
            name='embed_galleries',
            field=models.BooleanField(default=False, verbose_name='Embed galleries in page'),
        ),
    ]
