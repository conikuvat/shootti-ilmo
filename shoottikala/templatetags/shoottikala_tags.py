from django import template


register = template.Library()


def get_value(form, field_name):
    field = form.fields[field_name]
    value = form.initial[field_name]

    if getattr(field, 'choices', None):
        return dict(field.choices).get(value, value)
    else:
        return value


@register.inclusion_tag('shoottikala_readonly_form.jade')
def readonly(form):
    '''
    Renders a quick & dirty read only version of a ModelForm.
    '''

    fields = [(field, get_value(form, field_name)) for (field_name, field) in form.fields.items()]

    return dict(fields=fields)
