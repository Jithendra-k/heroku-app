from django import forms
from django.forms import ModelForm
from .models import Song


class SongForm(ModelForm):
    class Meta:
        model = Song
        fields = ['song_name', 'song_genre']
