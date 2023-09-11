from django import forms
from groups.models import group

class group_form(forms.ModelForm):
    class Meta:
        model = group
        fields = '__all__'