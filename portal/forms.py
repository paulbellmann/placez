# -*- coding: utf-8 -*-

from django import forms

class PointForm(forms.Form):
    title = forms.CharField(
        label='Titel',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Mein Ziel'})
    )

    city = forms.CharField(
        label='Stadt', 
        max_length=100, 
        widget=forms.TextInput(attrs={'placeholder': 'gewuenschte Stadt'})
    )

    street = forms.CharField(
        label='Straße',
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'gewuenschte Strasse'})
    )

    visited = forms.TypedChoiceField(
        label = "Visited?",
        choices = ((1, "Yes"), (0, "No")),
        coerce = lambda x: bool(int(x)),
        widget = forms.RadioSelect,
        initial = '0',
    )

    lat = forms.CharField(widget=forms.HiddenInput(), required=False)
    lng = forms.CharField(widget=forms.HiddenInput(), required=False)
