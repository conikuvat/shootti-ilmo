from django import forms

from .models import Photographer, Cosplayer


class PhotographerForm(forms.ModelForm):
    class Meta:
        model = Photographer
        fields = (
            'display_name',
            'introduction',
            'portfolio_links',
            'social_media_links',
        )


class CosplayerForm(forms.ModelForm):
    class Meta:
        model = Cosplayer
