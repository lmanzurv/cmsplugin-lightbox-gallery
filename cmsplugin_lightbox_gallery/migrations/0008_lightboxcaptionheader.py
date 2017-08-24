# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_urlconfrevision'),
        ('cmsplugin_lightbox_gallery', '0007_auto_20160719_1447'),
    ]

    operations = [
        migrations.CreateModel(
            name='LightboxCaptionHeader',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
            ],
            options={
                'verbose_name': 'Lightbox Caption Header',
                'verbose_name_plural': 'Lightbox Caption Headers',
            },
            bases=('cms.cmsplugin',),
        ),
    ]
