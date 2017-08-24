# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_lightbox_gallery', '0008_lightboxcaptionheader'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lightboxgallery',
            name='gallery_id',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Gallery ID', validators=[django.core.validators.RegexValidator(b'^([a-zA-Z0-9]+)$', message='The gallery ID must be alphanumeric', code=b'invalid_gallery_id')]),
        ),
    ]
