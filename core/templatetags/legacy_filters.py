from django import template
from django.template.defaultfilters import length

register = template.Library()

@register.filter
def length_is(value, arg):
    """
    Filtro length_is para compatibilidade com Django 5.0+
    Substitui o filtro removido do Django
    """
    try:
        return length(value) == int(arg)
    except (ValueError, TypeError):
        return False

@register.filter  
def divisibleby(value, arg):
    """
    Filtro divisibleby para compatibilidade com Django 5.0+
    """
    try:
        return int(value) % int(arg) == 0
    except (ValueError, TypeError, ZeroDivisionError):
        return False
