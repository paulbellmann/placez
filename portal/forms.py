# -*- coding: utf-8 -*-

from django import forms

class PointForm(forms.Form):
    title = forms.CharField(label='Titel', max_length=100)
    title.widget.attrs = {
        'placeholder': 'Mein Ziel',
    }
    city = forms.CharField(
        label='Stadt', 
        max_length=100, 
        widget=forms.TextInput(attrs={'placeholder': 'gewuenschte Stadt'})
    )

    street = forms.CharField(label='Straße', max_length=100, required=False)
    street.widget.attrs = {
        'placeholder': 'gewuenschte Strasse',
    }
    visited = forms.TypedChoiceField(
        label = "Visited?",
        choices = ((1, "Yes"), (0, "No")),
        coerce = lambda x: bool(int(x)),
        widget = forms.RadioSelect,
        initial = '0',
        required = True,
    )
    # postal = forms.IntegerField(label='PLZ')
    lat = forms.CharField(widget=forms.HiddenInput(), required=False)
    lng = forms.CharField(widget=forms.HiddenInput(), required=False)


class NameForm(forms.Form):
    first_name = forms.CharField(label='first name', max_length=100)
    last_name = forms.CharField(label='last name', max_length=100)

    like_website = forms.TypedChoiceField(
        label = "Do you like this website?",
        choices = ((1, "Yes"), (0, "No")),
        coerce = lambda x: bool(int(x)),
        widget = forms.RadioSelect,
        initial = '1',
        required = True,
    )

    favorite_food = forms.CharField(
        label = "What is your favorite food?",
        max_length = 80,
        required = True,
    )

    favorite_color = forms.CharField(
        label = "What is your favorite color?",
        max_length = 80,
        required = True,
    )

    favorite_number = forms.IntegerField(
        label = "Favorite number",
        required = False,
    )

    notes = forms.CharField(
        label = "Additional notes or feedback",
        required = False,
    )