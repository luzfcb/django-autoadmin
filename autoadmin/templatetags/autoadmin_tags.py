from __future__ import unicode_literals

from django.template import Library

from ..models import AutoAdminSingleton

register = Library()


@register.simple_tag(takes_context=True)
def autoadmin_properties(context):
    context['autoadmin_properties'] = AutoAdminSingleton.objects.get()
    return ''


@register.inclusion_tag('autoadmin/base.html')
def autoadmin_partial():
    return {'autoadmin_properties': AutoAdminSingleton.objects.get()}
