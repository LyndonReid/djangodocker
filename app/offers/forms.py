from django import forms

BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]

class SimpleForm(forms.Form):
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    favorite_colors = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=FAVORITE_COLORS_CHOICES,
    )

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    ASDF = forms.CharField(label='Your name', max_length=100)
    your_name = forms.CharField(label='Your name', max_length=100)
    ASDF = forms.CharField(label='Your name', max_length=100)