from django import template


register = template.Library()



@register.filter()
def censor(value):
    a = value.replace('редиска', 'р******')
    return f'{a}'