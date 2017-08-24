# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import aldryn_bootstrap3.model_fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_urlconfrevision'),
        ('cmsplugin_lightbox_gallery', '0005_auto_20160610_2058'),
    ]

    operations = [
        migrations.CreateModel(
            name='LightboxGalleryToggle',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('label', models.CharField(default=b'View Gallery', max_length=250, verbose_name='Label')),
                ('gallery_id', models.CharField(default=b'id', max_length=50, verbose_name='Target Gallery ID')),
                ('icon_left', aldryn_bootstrap3.model_fields.Icon(default='', max_length=255, blank=True)),
                ('icon_right', aldryn_bootstrap3.model_fields.Icon(default='', max_length=255, blank=True)),
                ('button_classes', models.CharField(max_length=250, null=True, verbose_name='CSS classes', blank=True)),
            ],
            options={
                'verbose_name': 'Lightbox Gallery Toggle',
                'verbose_name_plural': 'Lightbox Gallery Toggles',
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.AddField(
            model_name='lightboxgallery',
            name='gallery_id',
            field=models.CharField(max_length=50, null=True, verbose_name='Gallery ID', blank=True),
        ),
    ]
