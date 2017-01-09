from django import forms

from shoottikala.utils import horizontal_form_helper

from .models import User


class UserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

        self.helper = horizontal_form_helper()
        self.form_tag = None

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'nick',
            'email',
            # 'phone',
        )
