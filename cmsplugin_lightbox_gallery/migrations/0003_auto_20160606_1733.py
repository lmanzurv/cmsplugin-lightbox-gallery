# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_urlconfrevision'),
        ('cmsplugin_lightbox_gallery', '0002_auto_20160603_0936'),
    ]

    operations = [
        migrations.CreateModel(
            name='LightboxGalleryOverview',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
            ],
            options={
                'verbose_name': 'Lightbox Gallery Overview',
                'verbose_name_plural': 'Lightbox Gallery Overviews',
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.AlterField(
            model_name='lightboxgallery',
            name='name',
            field=models.CharField(default='Lightbox Gallery', max_length=250, verbose_name='Gallery name'),
        ),
        migrations.AddField(
            model_name='lightboxgalleryoverview',
            name='galleries',
            field=models.ManyToManyField(to='cmsplugin_lightbox_gallery.LightboxGallery'),
        ),
    ]
