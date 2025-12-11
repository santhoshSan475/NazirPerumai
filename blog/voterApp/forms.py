from .models import VoterDetails
from django import forms


class VoterForm(forms.ModelForm):
    class Meta:
        model = VoterDetails
        fields = "__all__"
