# myapp/forms.py
from django import forms

class GCDLCMForm(forms.Form):
    A = forms.IntegerField(label='A', min_value=1, max_value=100)
    B = forms.IntegerField(label='B', min_value=1, max_value=100)
