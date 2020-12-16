from django import forms
from .models import *


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('lastName', 'firstName', 'birthday', 'contact', 'email', 'relativeContact', 'pathologies', 'information')


class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ('pill', 'duration_start', 'duration_end', 'frequency_period', 'frequency_rel_period', 'quantity', 'otherFill')
