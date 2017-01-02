from django import forms

from .models import Photographer, Cosplayer
from .utils import horizontal_form_helper


class PhotographerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PhotographerForm, self).__init__(*args, **kwargs)

        self.helper = horizontal_form_helper()
        self.helper.form_tag = False

    class Meta:
        model = Photographer
        fields = (
            'display_name',
            'introduction',
            'portfolio_links',
            'social_media_links',
        )


class CosplayerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CosplayerForm, self).__init__(*args, **kwargs)

        self.helper = horizontal_form_helper()
        self.helper.form_tag = False

    class Meta:
        model = Cosplayer
        fields = (
            'display_name',
            'introduction',
            'source',
            'source_type',
            'character',
            'what_kinda_photos',
            'reference_links',
            'wip_links',
        )
