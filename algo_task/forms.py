from django import forms
from django.forms import ModelForm
from .models import AlgoTask


class CreateAbcForm(ModelForm):
    # task = forms.CharField(widget=forms.Textarea({'cols': '60', 'rows': "3"}))
    # task.widget.attrs.update({'cols': '40', 'rows': "2"})

    class Meta:
        model = AlgoTask
        fields = '__all__'
        # fields = ['task', 'a', 'b','c']
        print('\nfields: ', fields)
