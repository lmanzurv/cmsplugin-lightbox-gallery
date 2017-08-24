# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import force_text
from django.templatetags.static import static
from django.contrib.admin import StackedInline
from cms.plugin_base import CMSPluginBase
# from cms.models.pluginmodel import CMSPlugin
from cms.plugin_pool import plugin_pool
from .models import LightboxGallery, LightboxGalleryToggle, LightboxGalleryImage, LightboxCaptionHeader, LightboxCaptionFooter
from .models import LightboxVideo, LightboxGalleryOverview, LightboxSlider
from .models import LightboxGalleryImageGroup, LightboxGalleryImageInGroup

class LightboxGalleryPlugin(CMSPluginBase):
    model = LightboxGallery
    name = _('Lightbox Gallery')
    module = _('Lightbox')
    change_form_template = 'admin/gallery.html'
    render_template = 'lightbox_gallery.html'
    allow_children = True
    child_classes = ['LightboxGalleryImagePlugin', 'LightboxGalleryImageGroupPlugin', 'LightboxCaptionHeaderPlugin', 'LightboxCaptionFooterPlugin']

    fieldsets = (
        (None, {
            'fields': [
                'name',
                'gallery_id'
            ]
        }),
        (_('Launch Button'), {
            'fields': [
                'button_text',
                'button_icon_left',
                'button_icon_right',
                'button_classes'
            ]
        }),
        (_('More'), {
            'classes': ('collapse',),
            'fields': [
                'has_preview',
                'preview_amount',
                'rotating_images',
                'vertical_caption',
                'vertical_caption_more'
            ]
        })
    )

    def render(self, context, instance, placeholder):
        context = super(LightboxGalleryPlugin, self).render(context, instance, placeholder)

        from django.db.models import F
        image_groups = instance.image_groups()
        images_in_groups = LightboxGalleryImageInGroup.objects.only('id', 'image') \
            .filter(image_group_id__in=image_groups.values_list('id', flat=True)) \
            .annotate(position=F('image_group__cmsplugin_ptr__position')) \
            .order_by('image_group__cmsplugin_ptr__position', 'id')

        images = instance.images()

        from operator import attrgetter
        from itertools import chain
        if instance.has_preview:
            all_images = sorted(chain(images, images_in_groups), key=attrgetter('position'))

            number_images = len(all_images)
            preview_amount = instance.preview_amount
            context['more_images'] = (number_images - preview_amount) if preview_amount <= number_images else 0

            context['preview_images'] = all_images[:preview_amount]

        plugins = sorted(chain(images, image_groups), key=attrgetter('position'))
        context['images'] = plugins
        return context

plugin_pool.register_plugin(LightboxGalleryPlugin)

class LightboxGalleryTogglePlugin(CMSPluginBase):
    model = LightboxGalleryToggle
    name = _('Lightbox Gallery Toggle')
    module = _('Lightbox')
    change_form_template = 'admin/gallery_toggle.html'
    render_template = 'lightbox_gallery_toggle.html'
    text_enabled = True

    def render(self, context, instance, placeholder):
        context = super(LightboxGalleryTogglePlugin, self).render(context, instance, placeholder)
        return context

    def icon_src(self, instance):
        return static('lightbox_gallery/img/toggle.png')

    def icon_alt(self, instance):
        return '%s - %s' % (force_text(self.name), instance.gallery_id)

plugin_pool.register_plugin(LightboxGalleryTogglePlugin)

class LightboxGalleryImagePlugin(CMSPluginBase):
    model = LightboxGalleryImage
    name = _('Lightbox Image')
    module = _('Lightbox')
    render_template = 'lightbox_gallery_image.html'
    require_parent = True
    parent_classes = ['LightboxGalleryPlugin', 'LightboxSliderPlugin']

    fieldsets = (
        (None, {
            'fields': [
                'image',
                'description',
            ]
        }),
        (_('Image resizing options'), {
            'fields': [
                'use_original_image',
                ('width', 'height',),
                ('crop', 'upscale',),
                'thumbnail_option',
                'use_autoscale',
            ]
        })
    )

    def _get_thumbnail_options(self, context, instance):
        """
        Return the size and options of the thumbnail that should be inserted
        """
        width, height = None, None
        crop, upscale = False, False
        subject_location = False
        placeholder_width = context.get('width', None)
        placeholder_height = context.get('height', None)
        if instance.thumbnail_option:
            # thumbnail option overrides everything else
            if instance.thumbnail_option.width:
                width = instance.thumbnail_option.width
            if instance.thumbnail_option.height:
                height = instance.thumbnail_option.height
            crop = instance.thumbnail_option.crop
            upscale = instance.thumbnail_option.upscale
        else:
            if instance.use_autoscale and placeholder_width:
                # use the placeholder width as a hint for sizing
                width = int(placeholder_width)
            elif instance.width:
                width = instance.width
            if instance.use_autoscale and placeholder_height:
                height = int(placeholder_height)
            elif instance.height:
                height = instance.height
            crop = instance.crop
            upscale = instance.upscale
        if instance.image:
            if instance.image.subject_location:
                subject_location = instance.image.subject_location
            if not height and width:
                # height was not externally defined: use ratio to scale it by the width
                height = int(float(width) * float(instance.image.height) / float(instance.image.width))
            if not width and height:
                # width was not externally defined: use ratio to scale it by the height
                width = int(float(height) * float(instance.image.width) / float(instance.image.height))
            if not width:
                # width is still not defined. fallback the actual image width
                width = instance.image.width
            if not height:
                # height is still not defined. fallback the actual image height
                height = instance.image.height
        return {'size': (width, height),
                'crop': crop,
                'upscale': upscale,
                'subject_location': subject_location}

    def render(self, context, instance, placeholder):
        context = super(LightboxGalleryImagePlugin, self).render(context, instance, placeholder)
        options = self._get_thumbnail_options(context, instance)
        context.update({
            'opts': options,
            'parent': instance.parent.plugin_type
        })
        return context

plugin_pool.register_plugin(LightboxGalleryImagePlugin)

class LightboxCaptionHeaderPlugin(CMSPluginBase):
    model = LightboxCaptionHeader
    name = _('Lightbox Caption Header')
    module = _('Lightbox')
    render_template = 'lightbox_caption_header.html'
    require_parent = True
    parent_classes = ['LightboxGalleryPlugin']
    allow_children = True

    def render(self, context, instance, placeholder):
        context = super(LightboxCaptionHeaderPlugin, self).render(context, instance, placeholder)
        return context

plugin_pool.register_plugin(LightboxCaptionHeaderPlugin)

class LightboxCaptionFooterPlugin(CMSPluginBase):
    model = LightboxCaptionFooter
    name = _('Lightbox Caption Footer')
    module = _('Lightbox')
    render_template = 'lightbox_caption_footer.html'
    require_parent = True
    parent_classes = ['LightboxGalleryPlugin']
    allow_children = True

    def render(self, context, instance, placeholder):
        context = super(LightboxCaptionFooterPlugin, self).render(context, instance, placeholder)
        return context

plugin_pool.register_plugin(LightboxCaptionFooterPlugin)

class LightboxVideoPlugin(CMSPluginBase):
    model = LightboxVideo
    name = _('Lightbox Video')
    module = _('Lightbox')
    render_template = 'lightbox_video.html'
    change_form_template = 'admin/video.html'

    def render(self, context, instance, placeholder):
        context = super(LightboxVideoPlugin, self).render(context, instance, placeholder)
        return context

plugin_pool.register_plugin(LightboxVideoPlugin)

class LightboxGalleryOverviewPlugin(CMSPluginBase):
    model = LightboxGalleryOverview
    name = _('Lightbox Gallery Overview')
    module = _('Lightbox')
    render_template = 'lightbox_gallery_overview.html'

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == 'galleries':
            language = request.GET.get('plugin_language')

            if 'language' in self._cms_initial_attributes:
                language = self._cms_initial_attributes.get('language')

            if not language and self.cms_plugin_instance:
                language = self.cms_plugin_instance.language

            if not language:
                language = request.GET.get('cms_path')
                if language:
                    language = language.split('/')[1]

            if not language:
                language = request.GET.get('LANGUAGE_CODE')

            kwargs['queryset'] = LightboxGallery.objects.filter(placeholder__page__publisher_is_draft=True,
                language=language)
        return super(LightboxGalleryOverviewPlugin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def render(self, context, instance, placeholder):
        context = super(LightboxGalleryOverviewPlugin, self).render(context, instance, placeholder)
        galleries = list()
        for gallery in instance.galleries.all():
            images = gallery.images()
            galleries.append(dict(id=gallery.id, gallery_id=gallery.gallery_id, gallery=gallery, vertical_caption=True, number_images=images.count(),
                vertical_caption_more=gallery.vertical_caption_more, cover_image=images[0].image if images.exists() else None,
                page=gallery.cmsplugin_ptr.placeholder.page.get_absolute_url()))
        #     caption_header = LightboxCaptionHeader.objects.filter(cmsplugin_ptr__parent=gallery)
        #     caption_header = caption_header[0] if caption_header.count() > 0 else None
        #     if caption_header:
        #         caption_header.child_plugin_instances = list(CMSPlugin.objects.filter(parent_id=caption_header.id))
        #     caption_footer = LightboxCaptionFooter.objects.filter(cmsplugin_ptr__parent=gallery)
        #     caption_footer = caption_footer[0] if caption_footer.count() > 0 else None
        #     if caption_footer:
        #         caption_footer.child_plugin_instances = list(CMSPlugin.objects.filter(parent_id=caption_footer.id))
        context['galleries'] = galleries
        return context

plugin_pool.register_plugin(LightboxGalleryOverviewPlugin)

class LightboxSliderPlugin(CMSPluginBase):
    model = LightboxSlider
    name = _('Lightbox Slider')
    module = _('Lightbox')
    render_template = 'lightbox_slider.html'
    allow_children = True
    child_classes = ['LightboxGalleryImagePlugin']

    def render(self, context, instance, placeholder):
        context = super(LightboxSliderPlugin, self).render(context, instance, placeholder)
        return context

plugin_pool.register_plugin(LightboxSliderPlugin)

class LightboxGalleryImageInGroupInline(StackedInline):
    model = LightboxGalleryImageInGroup
    extra = 0

class LightboxGalleryImageGroupPlugin(CMSPluginBase):
    model = LightboxGalleryImageGroup
    inlines = [LightboxGalleryImageInGroupInline]
    name = _('Lightbox Image Group')
    module = _('Lightbox')
    render_template = 'lightbox_gallery_image_group.html'
    require_parent = True
    parent_classes = ['LightboxGalleryPlugin', 'LightboxSliderPlugin']

    fieldsets = (
        (None, {'fields': []}),
        (_('Image resizing options'), {
            'fields': [
                'use_original_image',
                ('width', 'height',),
                ('crop', 'upscale',),
                'thumbnail_option',
                'use_autoscale',
            ]
        }),
        (_('Images'), {'fields': []})
    )

    def _get_thumbnail_options(self, context, instance):
        """
        Return the size and options of the thumbnail that should be inserted
        """
        width, height = None, None
        crop, upscale = False, False
        placeholder_width = context.get('width', None)
        placeholder_height = context.get('height', None)
        if instance.thumbnail_option:
            # thumbnail option overrides everything else
            if instance.thumbnail_option.width:
                width = instance.thumbnail_option.width
            if instance.thumbnail_option.height:
                height = instance.thumbnail_option.height
            crop = instance.thumbnail_option.crop
            upscale = instance.thumbnail_option.upscale
        else:
            if instance.use_autoscale and placeholder_width:
                # use the placeholder width as a hint for sizing
                width = int(placeholder_width)
            elif instance.width:
                width = instance.width
            if instance.use_autoscale and placeholder_height:
                height = int(placeholder_height)
            elif instance.height:
                height = instance.height
            crop = instance.crop
            upscale = instance.upscale

        return {'size': (width, height),
                'crop': crop,
                'upscale': upscale}

    def render(self, context, instance, placeholder):
        context = super(LightboxGalleryImageGroupPlugin, self).render(context, instance, placeholder)
        thumb_options = self._get_thumbnail_options(context, instance)
        context.update({
            'thumb_options': thumb_options,
            'parent': instance.parent
        })
        return context

plugin_pool.register_plugin(LightboxGalleryImageGroupPlugin)
