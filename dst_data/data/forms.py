from django import forms

class SearchForm(forms.Form):
    date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))