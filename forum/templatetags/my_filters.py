from django import template
register = template.Library()


# This adds the ability to add classes to forms.
# add {% load my_filters %} to html to load these filters

@register.filter(name='addclass')
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg})
