from django import forms
from opendata_tw import models


class MusicalActivityForm(forms.ModelForm):

    class Meta:
        model = models.MusicalActivity
        fields = '__all__'
