from django import template
register = template.Library()

@register.filter(name='cut_name')
def cut_name(text):
    return text[text.find("|") + 1:]
@register.filter(name='cut_prog')
def cut_prog(text):
    return text[:text.find("|")]
