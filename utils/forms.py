from django.forms import ModelForm
from .models import PrivateGenome


class PrivateGenomeForm(ModelForm):
    class Meta:
        model = PrivateGenome
        fields = ['sequence_file', 'annotation_file']
