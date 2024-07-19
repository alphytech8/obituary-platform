from django import forms
from .models import Obituary

class ObituaryForm(forms.ModelForm):
    class Meta:
        model = Obituary
        fields = ['name', 'birth_date', 'death_date', 'biography', 'photo', 'seo_title', 'seo_description', 'social_media_tags']
