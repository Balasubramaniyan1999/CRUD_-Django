from django import forms
from .models import RegisterForms

class MyRegisterForm(forms.ModelForm):
    class Meta:
        model = RegisterForms
        fields = ["name","age","address","contact","email"]