# -*- coding: utf-8 -*-
from django import template
from cms.models.pluginmodel import CMSPlugin

register = template.Library()

@register.filter
def isplugin(obj):
    return isinstance(obj, CMSPlugin)

@register.filter
def imagesize(image, thumb_size):
    width, height = thumb_size
    if image:
        if not height and width:
            # height was not externally defined: use ratio to scale it by the width
            height = int(float(width) * float(image.height) / float(image.width))
        if not width and height:
            # width was not externally defined: use ratio to scale it by the height
            width = int(float(height) * float(image.width) / float(image.height))
        if not width:
            # width is still not defined. fallback the actual image width
            width = image.width
        if not height:
            # height is still not defined. fallback the actual image height
            height = image.height

    return (width, height)
