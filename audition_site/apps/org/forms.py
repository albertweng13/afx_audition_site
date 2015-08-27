from django import forms
from .models import Dancer

class DancerForm(forms.ModelForm):
    class Meta:
        model = Dancer
        fields = (
            'org',
            'name',
            'email',
        )