from django import forms
from .models import Genre


class AddTrackForm(forms.Form):
    track_name = forms.CharField(label='Track Name', max_length=200, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Track Name'}))
    track_rating = forms.FloatField(label='Rating', max_value=5,widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Rating'}))
    genre = forms.ModelMultipleChoiceField(queryset=Genre.objects.all(), required=False, widget=forms.CheckboxSelectMultiple)


class AddGenreForm(forms.ModelForm):
    genre_name = forms.CharField(label='Genre Name', max_length=200, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Genre Name'}))

    class Meta:
        model = Genre
        fields = ['genre_name']