from django import template


register = template.Library()

# @register.filter(name='add_comma')
# def add_comma(value, arg):
#     return value.replace(arg, '')


@register.filter(name="cut")
def cut(value, arg):
    """Removes all values of arg from the given string"""
    return value.replace(arg, "")