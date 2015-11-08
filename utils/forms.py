from django import forms
from django.forms import ModelForm
from .models import PrivateGenome


class PrivateGenomeForm(ModelForm):
    class Meta:
        model = PrivateGenome
        fields = ['name', 'document_file', 'sequence_file', 'annotation_file']

    def clean(self):
        cleaned_data = super(PrivateGenomeForm, self).clean()

        for _file in ["sequence_file", "annotation_file"]:
            if cleaned_data.get(_file) is None:
                raise forms.ValidationError(
                    "{} is needed!".format(_file.replace('_', ' '))
                )
        return cleaned_data
