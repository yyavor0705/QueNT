from django import forms
from djUI.models import Company


class NewCompany(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'

