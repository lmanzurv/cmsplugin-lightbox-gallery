# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_urlconfrevision'),
        ('cmsplugin_lightbox_gallery', '0003_auto_20160606_1733'),
    ]

    operations = [
        migrations.CreateModel(
            name='LightboxSlider',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('is_vertical', models.BooleanField(default=False, verbose_name='Vertical thumbnails')),
                ('autoplay', models.BooleanField(default=True, verbose_name='Autoplay')),
                ('pause_hover', models.BooleanField(default=True, verbose_name='Pause on hover')),
                ('adaptive_height', models.BooleanField(default=False, verbose_name='Adaptive height')),
            ],
            options={
                'verbose_name': 'Lightbox Slider',
                'verbose_name_plural': 'Lightbox Sliders',
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.AlterModelOptions(
            name='lightboxgalleryimage',
            options={'verbose_name': 'Lightbox Image', 'verbose_name_plural': 'Lightbox Images'},
        ),
    ]
