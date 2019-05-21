from django import template
from django.utils.safestring import mark_safe
register = template.Library()
#register是固定变量名，不能改变

#自定义标签，不能用于if语句
@register.simple_tag()
def my_add100(v1):
    return v1+100

#自定义filter
@register.filter()
def my_add100(v1, v2):
    return v1+v2
