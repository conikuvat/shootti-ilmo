import datetime
from django import template


register = template.Library()


@register.inclusion_tag('shoottikala_readonly_form.jade')
def readonly(form):
    '''
    Renders a quick & dirty read only version of a ModelForm.
    '''

    fields = [(field, form.initial[field_name]) for (field_name, field) in form.fields.items()]

    return dict(fields=fields)
