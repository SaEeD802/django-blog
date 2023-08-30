from django import template
import datetime

register = template.Library()

# baraye import -> {% load filters %}

@register.filter
def cutter(value, arg):
    return value[:arg]
# baraye namayesh dar template -> <p>{{ recent.body|cutter:160 }}</p>


@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)
# baraye namayesh dar template ->  <span>{% current_time "%Y-%m-%d" %}</span>