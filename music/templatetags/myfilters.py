from django.template import Library
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe, SafeData
from django.utils.text import normalize_newlines
from django.utils.html import escape


register = Library()


@register.filter(is_safe=True, needs_autoescape=True)
@stringfilter
def keep_spacing(value, autoescape=None):
    autoescape = autoescape and not isinstance(value, SafeData)
    value = normalize_newlines(value)
    if autoescape:
        value = escape(value)
    value = mark_safe(value.replace('  ', ' &nbsp;'))
    return '&nbsp; &nbsp; &nbsp; &nbsp;' + mark_safe(value.replace('\n', '<br />'))


@register.filter()
@stringfilter
def get_str(value):
    temp = keep_spacing(value)
    length = len(temp)
    return temp[:int(0.5 * length)]+'...'
