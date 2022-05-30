from django import forms
from .models import Team

# class FormNameModel(forms.ModelForm)

class Query(forms.Form):
    search_input = forms.CharField()



class NewUserForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = '__all__'
