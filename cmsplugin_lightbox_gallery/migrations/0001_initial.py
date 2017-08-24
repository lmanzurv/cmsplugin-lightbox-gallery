# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_urlconfrevision'),
        ('filer', '0002_auto_20150606_2003'),
    ]

    operations = [
        migrations.CreateModel(
            name='LightboxGallery',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('button_classes', models.CharField(max_length=250, null=True, verbose_name='Launch Gallery Button Classes', blank=True)),
            ],
            options={
                'verbose_name': 'Lightbox Gallery',
                'verbose_name_plural': 'Lightbox Galleries',
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='LightboxGalleryImage',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('description', models.CharField(max_length=250, null=True, verbose_name='Image text', blank=True)),
                ('image', filer.fields.image.FilerImageField(verbose_name='Image', to='filer.Image')),
            ],
            options={
                'verbose_name': 'Lightbox Gallery Image',
                'verbose_name_plural': 'Lightbox Gallery Images',
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='LightboxVideo',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('overlay', models.BooleanField(default=True, verbose_name='Video as overlay')),
                ('button_classes', models.CharField(max_length=250, null=True, verbose_name='Watch Video Button Classes', blank=True)),
                ('url', models.URLField(max_length=250, verbose_name='Video URL')),
            ],
            options={
                'verbose_name': 'Lightbox Video',
                'verbose_name_plural': 'Lightbox Videos',
            },
            bases=('cms.cmsplugin',),
        ),
    ]
