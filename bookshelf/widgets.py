# -*- coding: utf-8 -*-
"""
widgets for django-form-utils

This code is from https://github.com/carljm/django-form-utils/blob/master/form_utils/widgets.py

parts of this code taken from http://www.djangosnippets.org/snippets/934/
 - thanks baumer1122

"""
from __future__ import unicode_literals

import posixpath

from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe

from .settings import JQUERY_URL

try:
    from sorl.thumbnail import get_thumbnail

    def thumbnail(image_path, width, height):
        geometry_string = 'x'.join([str(width), str(height)])
        t = get_thumbnail(image_path, geometry_string)
        return u'<img src="%s" alt="%s" />' % (t.url, image_path)
except ImportError:
    try:
        from easy_thumbnails.files import get_thumbnailer

        def thumbnail(image_path, width, height):
            thumbnail_options = dict(size=(width, height), crop=True)
            thumbnail = get_thumbnailer(image_path).get_thumbnail(
                thumbnail_options)
            return u'<img src="%s" alt="%s" />' % (thumbnail.url, image_path)
    except ImportError:
        def thumbnail(image_path, width, height):
            absolute_url = posixpath.join(settings.MEDIA_URL, image_path)
            return u'<img src="%s" alt="%s" />' % (absolute_url, image_path)


class ImageWidget(forms.FileInput):
    template = '%(input)s<br />%(image)s'

    def __init__(self, attrs=None, template=None, width=200, height=300):
        if template is not None:
            self.template = template
        self.width = width
        self.height = height
        super(ImageWidget, self).__init__(attrs)

    def render(self, name, value, attrs=None):
        input_html = super(ImageWidget, self).render(name, value, attrs)
        if hasattr(attrs, 'width') and hasattr(attrs, 'height') and hasattr(value, 'name'):
            image_html = thumbnail(value.name, attrs['width'], attrs['height'])
        elif hasattr(value, 'name'):
            image_html = thumbnail(value.name, self.width, self.height)
        else:
            image_html = ''
        output = self.template % {'input': input_html, 'image': image_html}
        # else:
        #     output = input_html
        return mark_safe(output)


class ClearableFileInput(forms.MultiWidget):
    default_file_widget_class = forms.FileInput
    template = '%(input)s Clear: %(checkbox)s'

    def __init__(self, file_widget=None,
                 attrs=None, template=None):
        if template is not None:
            self.template = template
        file_widget = file_widget or self.default_file_widget_class()
        super(ClearableFileInput, self).__init__(
            widgets=[file_widget, forms.CheckboxInput()],
            attrs=attrs)

    def render(self, name, value, attrs=None):
        if isinstance(value, list):
            self.value = value[0]
        else:
            self.value = value
        return super(ClearableFileInput, self).render(name, value, attrs)

    def decompress(self, value):
        # the clear checkbox is never initially checked
        return [value, None]

    def format_output(self, rendered_widgets):
        if self.value:
            return self.template % {'input': rendered_widgets[0],
                                    'checkbox': rendered_widgets[1]}
        return rendered_widgets[0]


root = lambda path: posixpath.join(settings.STATIC_URL, path)


class AutoResizeTextarea(forms.Textarea):
    """
    A Textarea widget that automatically resizes to accomodate its contents.
    """

    class Media:
        js = (JQUERY_URL,
              root('form_utils/js/jquery.autogrow.js'),
              root('form_utils/js/autoresize.js'))

    def __init__(self, *args, **kwargs):
        attrs = kwargs.setdefault('attrs', {})
        try:
            attrs['class'] = "%s autoresize" % (attrs['class'],)
        except KeyError:
            attrs['class'] = 'autoresize'
        attrs.setdefault('cols', 80)
        attrs.setdefault('rows', 5)
        super(AutoResizeTextarea, self).__init__(*args, **kwargs)


class InlineAutoResizeTextarea(AutoResizeTextarea):
    def __init__(self, *args, **kwargs):
        attrs = kwargs.setdefault('attrs', {})
        try:
            attrs['class'] = "%s inline" % (attrs['class'],)
        except KeyError:
            attrs['class'] = 'inline'
        attrs.setdefault('cols', 40)
        attrs.setdefault('rows', 2)
        super(InlineAutoResizeTextarea, self).__init__(*args, **kwargs)

#
# class AddSelectWidget(forms.Widget):
#     def __init__(self, attrs=None, choices=(), entity_name=None, is_aux=False, parent=None):
#         super(AddSelectWidget, self).__init__(attrs)
#
#         self.choices = choices
#         self.entity_name = entity_name
#         self.is_aux = is_aux
#         self.parent = parent
#
#     def value_from_datadict(self, data, files, name):
#         value = super(AddSelectWidget, self).value_from_datadict(data, files, name)
#         self.data = data
#         return value
#
#     def render(self, name, value, attrs=None, choices=()):
#         if not hasattr(self, 'data'):
#             self.data = {}
#         if value is None:
#             value = ''
#         final_attrs = self.build_attrs(attrs)
#         output = [u"<select%s name='%s'>" % (flatatt(final_attrs), name)]
#         options = self.render_options(choices, [value], name)
#         if options:
#             output.append(options)
#         output.append('</select>')
#         output.append(self.add_button_string() % {
#             'url': self.generate_url(),
#             'object_id': self.build_attrs(attrs)['id'],
#             'entity': name,
#         })
#         return mark_safe(u'\n'.join(output))
#
#     def render_options(self, choices, selected_choices, name):
#         selected_choices = set(force_unicode(v) for v in selected_choices)
#         output = []
#         for option_value, option_label in chain(self.choices, choices):
#             if isinstance(option_label, (list, tuple)):
#                 for option in option_label:
#                     output.append(self.render_option(name, selected_choices, *option))
#             else:
#                 output.append(self.render_option(name, selected_choices, option_value, option_label))
#         return u'\n'.join(output)
#
#     def render_option(self, name, selected_choices, option_value, option_label):
#         option_value = force_unicode(option_value)
#         data = self.data.copy()
#         data[name] = option_value
#         selected = data == self.data or option_value in selected_choices
#         return self.option_string() % {
#             'attrs': selected and ' selected="selected"' or '',
#             'value': option_value,
#             'label': force_unicode(option_label)
#         }
#
#     def option_string(self):
#         return '<option value="%(value)s" %(attrs)s>%(label)s</option>'
#
#     def add_button_string(self):
#         return '<a class="btn-plus" onclick="launchAddButton(\'%(url)s\', \'%(object_id)s \', \'%(entity)s \')"><i class="icon-plus"></i></a>'
#
#     def generate_url(self):
#         return '/app/widget/create/%s' % self.entity_name
