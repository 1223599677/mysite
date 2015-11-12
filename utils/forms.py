# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.forms import ModelForm
from .models import PrivateGenome, SequenceInfo


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


class SequenceInfoForm(forms.ModelForm):
    class Meta:
        model = SequenceInfo
        fields = ('strain', 'strain_owner', 'public_type', 'sequence_type', 'industrial_application',)

    '''
    def clean(self):
        cleaned_data = super(SequenceInfoForm, self).clean()
        return cleaned_data
    '''