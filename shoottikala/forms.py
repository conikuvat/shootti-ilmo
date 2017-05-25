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
            'days',
        )
        widgets = dict(
            days=forms.CheckboxSelectMultiple,
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
            'character',
            'source',
            'source_type',
            'what_kinda_photos',
            'reference_links',
            'wip_links',
            'social_media_links',
            'days',
        )
        widgets = dict(
            days=forms.CheckboxSelectMultiple,
        )


class MessageForm(forms.Form):
    message_text = forms.CharField(
        label='Viestin teksti',
        help_text=(
            'Viestin mukana toimitetaan automaattisesti sähköpostiosoitteesi sekä linkki '
            'ilmoitukseesi. Ilmoituksessasi olevia tietoja sinun ei tarvitse siis toistaa viestissäsi. '
            'Kannattaa jo tässä vaiheessa ehdottaa sinulle sopivia aikoja photoshootille.'
        ),
        widget=forms.Textarea,
    )

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)

        self.helper = horizontal_form_helper()
        self.helper.form_tag = False
