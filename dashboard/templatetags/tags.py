from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(field, css):
    """Removes all values of arg from the given string"""
    try:
        return field.as_widget(attrs={"class": css})
    except:
        pass