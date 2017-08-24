# -*- coding: utf-8 -*-
from django.db import models
from cms.models.pluginmodel import CMSPlugin
from filer.fields.image import FilerImageField
from django.utils.translation import ugettext_lazy as _
from aldryn_bootstrap3.model_fields import Icon
from django.core.validators import RegexValidator

class LightboxGallery(CMSPlugin):
    name = models.CharField(max_length=250, verbose_name=_('Gallery name'), default=_('Lightbox Gallery'))
    gallery_id = models.CharField(max_length=50, verbose_name=_('Gallery ID'), validators=[RegexValidator(r'^([a-zA-Z0-9]+)$',
        message=_('The gallery ID must be alphanumeric'), code='invalid_gallery_id')], null=True, blank=True)
    button_text = models.CharField(max_length=250, verbose_name=_('Launch gallery button label'), null=True, blank=True)
    button_icon_left = Icon()
    button_icon_right = Icon()
    button_classes = models.CharField(max_length=250, verbose_name=_('Launch gallery button classes'), null=True, blank=True)
    has_preview = models.BooleanField(default=False, verbose_name=_('Gallery has preview'))
    preview_amount = models.IntegerField(default=0, verbose_name=_('Amount of images for preview'), null=True, blank=True)
    rotating_images = models.IntegerField(default=0, verbose_name=_('Amount of images for rotating banner'), null=True, blank=True)
    vertical_caption = models.BooleanField(default=False, verbose_name=_('Vertical caption'))
    vertical_caption_more = models.CharField(max_length=250, verbose_name=_('Vertical caption view more'), null=True, blank=True)

    def images(self):
        return LightboxGalleryImage.objects.filter(cmsplugin_ptr__parent_id=self.id).order_by('cmsplugin_ptr__position')

    def image_groups(self):
        return LightboxGalleryImageGroup.objects.filter(cmsplugin_ptr__parent_id=self.id).order_by('cmsplugin_ptr__position')

    @property
    def caption_header(self):
        header = None
        if self.child_plugin_instances:
            for child in self.child_plugin_instances:
                if child.plugin_type == 'LightboxCaptionHeaderPlugin':
                    header = child
                    break
        return header

    @property
    def caption_footer(self):
        footer = None
        if self.child_plugin_instances:
            for child in self.child_plugin_instances:
                if child.plugin_type == 'LightboxCaptionFooterPlugin':
                    footer = child
                    break
        return footer

    class Meta:
        verbose_name = _('Lightbox Gallery')
        verbose_name_plural = _('Lightbox Galleries')

    def __unicode__(self):
        return '%s' % (self.name)

class LightboxGalleryToggle(CMSPlugin):
    label = models.CharField(max_length=250, verbose_name=_('Label'), default='View Gallery')
    gallery_id = models.CharField(max_length=50, verbose_name=_('Target Gallery ID'), default='id')
    icon_left = Icon()
    icon_right = Icon()
    button_classes = models.CharField(max_length=250, verbose_name=_('CSS classes'), null=True, blank=True)

    class Meta:
        verbose_name = _('Lightbox Gallery Toggle')
        verbose_name_plural = _('Lightbox Gallery Toggles')

    def __unicode__(self):
        return '%s' % self.label

class LightboxGalleryImage(CMSPlugin):
    image = FilerImageField(verbose_name=_('Image'))
    use_original_image = models.BooleanField(_('use the original image'), default=False, help_text=_('do not resize the image. use the original image instead.'))
    thumbnail_option = models.ForeignKey('filer.ThumbnailOption', null=True, blank=True, verbose_name=_('thumbnail option'),
        help_text=_('overrides width, height, crop and upscale with values from the selected thumbnail option'))
    use_autoscale = models.BooleanField(_('use automatic scaling'), default=False, help_text=_('tries to auto scale the image based on the placeholder context'))
    width = models.PositiveIntegerField(_('width'), null=True, blank=True)
    height = models.PositiveIntegerField(_('height'), null=True, blank=True)
    crop = models.BooleanField(_('crop'), default=True)
    upscale = models.BooleanField(_('upscale'), default=True)
    description = models.CharField(max_length=250, verbose_name=_('Image text'), null=True, blank=True)

    class Meta:
        verbose_name = _('Lightbox Image')
        verbose_name_plural = _('Lightbox Images')

    def __unicode__(self):
        return self.image.original_filename

class LightboxCaptionHeader(CMSPlugin):
    class Meta:
        verbose_name = _('Lightbox Caption Header')
        verbose_name_plural = _('Lightbox Caption Headers')

    def __unicode__(self):
        return ''

class LightboxCaptionFooter(CMSPlugin):
    class Meta:
        verbose_name = _('Lightbox Caption Footer')
        verbose_name_plural = _('Lightbox Caption Footers')

    def __unicode__(self):
        return ''

class LightboxVideo(CMSPlugin):
    overlay = models.BooleanField(default=True, verbose_name=_('Video as overlay'))
    button_classes = models.CharField(max_length=250, verbose_name=_('Watch video button classes'), null=True, blank=True)
    button_text = models.CharField(max_length=250, verbose_name=_('Watch video button label'), null=True, blank=True)
    button_icon_left = Icon()
    button_icon_right = Icon()
    poster = FilerImageField(verbose_name=_('Video poster'), null=True, blank=True)
    url = models.URLField(max_length=250, verbose_name=_('Video URL'))

    class Meta:
        verbose_name = _('Lightbox Video')
        verbose_name_plural = _('Lightbox Videos')

    def __unicode__(self):
        return self.url

class LightboxGalleryOverview(CMSPlugin):
    galleries = models.ManyToManyField(LightboxGallery)
    embed_galleries = models.BooleanField(default=False, verbose_name=_('Embed galleries in page'))

    def copy_relations(self, oldinstance):
        self.galleries = oldinstance.galleries.all()

    class Meta:
        verbose_name = _('Lightbox Gallery Overview')
        verbose_name_plural = _('Lightbox Gallery Overviews')

    def __unicode__(self):
        return '%d %s' % (self.galleries.count(), 'galleries' if self.galleries.count() > 1 else 'gallery')

class LightboxSlider(CMSPlugin):
    is_vertical = models.BooleanField(default=False, verbose_name=_('Vertical thumbnails'))
    autoplay = models.BooleanField(default=True, verbose_name=_('Autoplay'))
    pause_hover = models.BooleanField(default=True, verbose_name=_('Pause on hover'))
    adaptive_height = models.BooleanField(default=False, verbose_name=_('Adaptive height'))

    class Meta:
        verbose_name = _('Lightbox Slider')
        verbose_name_plural = _('Lightbox Sliders')

    def __unicode__(self):
        return ''


class LightboxGalleryImageGroup(CMSPlugin):
    use_original_image = models.BooleanField(_('use the original image'), default=False, help_text=_('do not resize the image. use the original image instead.'))
    thumbnail_option = models.ForeignKey('filer.ThumbnailOption', null=True, blank=True, verbose_name=_('thumbnail option'),
        help_text=_('overrides width, height, crop and upscale with values from the selected thumbnail option'))
    use_autoscale = models.BooleanField(_('use automatic scaling'), default=False, help_text=_('tries to auto scale the image based on the placeholder context'))
    width = models.PositiveIntegerField(_('width'), null=True, blank=True)
    height = models.PositiveIntegerField(_('height'), null=True, blank=True)
    crop = models.BooleanField(_('crop'), default=True)
    upscale = models.BooleanField(_('upscale'), default=True)

    @property
    def images(self):
        return LightboxGalleryImageInGroup.objects.filter(image_group_id=self.id)

    @property
    def images_count(self):
        return LightboxGalleryImageInGroup.objects.filter(image_group_id=self.id).count()

    def copy_relations(self, oldinstance):
        for image in oldinstance.image_group.all():
            image.pk = None
            image.image_group = self
            image.save()

    class Meta:
        verbose_name = _('Lightbox Image Group')
        verbose_name_plural = _('Lightbox Image Groups')

    def __unicode__(self):
        count = self.images_count
        return '%s images' % count if count != 1 else '1 image'

class LightboxGalleryImageInGroup(models.Model):
    image_group = models.ForeignKey(LightboxGalleryImageGroup, related_name='image_group')
    image = FilerImageField(verbose_name=_('Image'))
    description = models.CharField(max_length=250, verbose_name=_('Image text'), null=True, blank=True)

    @property
    def subject_location(self):
        return self.image.subject_location if self.image.subject_location else False

    class Meta:
        verbose_name = _('Lightbox Group Image')
        verbose_name_plural = _('Lightbox Group Images')

    def __unicode__(self):
        return self.image.original_filename
