from django import forms
from .models import Movie


class MovieForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Movie


