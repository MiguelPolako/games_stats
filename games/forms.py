from django import forms
from games import models
from django.core.exceptions import ValidationError


class GenreForm(forms.ModelForm):
    class Meta:
        model = models.Genre
        fields = '__all__'


class PublisherForm(forms.ModelForm):
    class Meta:
        model = models.Publisher
        fields = '__all__'


class PlatformForm(forms.ModelForm):
    class Meta:
        model = models.Platform
        fields = '__all__'


class GameForm(forms.ModelForm):
    class Meta:
        model = models.Game
        fields = '__all__'


