from django import template

register = template.Library()

@register.filter('cut')
def cut(value, arg):
    """
    This cuts all of values of "arg" from string!
    """
    return value.replace(arg, '')

# register.filte('cut', cut)