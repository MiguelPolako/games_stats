from django import forms
from games import models
from django.core.exceptions import ValidationError


class GenreForm(forms.ModelForm):
    class Meta:
        model = models.Genre
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }


class PublisherForm(forms.ModelForm):
    class Meta:
        model = models.Publisher
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'})
        }


class PlatformForm(forms.ModelForm):
    class Meta:
        model = models.Platform
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }


class GameForm(forms.ModelForm):
    class Meta:
        model = models.Game
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'year': forms.NumberInput(attrs={'class': 'form-control'}),
            'na_sales': forms.NumberInput(attrs={'class': 'form-control'}),
            'eu_sales': forms.NumberInput(attrs={'class': 'form-control'}),
            'jp_sales': forms.NumberInput(attrs={'class': 'form-control'}),
            'publisher': forms.Select(attrs={'class': 'form-control'}),
            'genres': forms.SelectMultiple(attrs={'class': 'selectpicker'}),
            'platform': forms.CheckboxSelectMultiple(
                attrs={'class': 'custom-control custom-checkbox'}),
        }
