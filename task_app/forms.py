from django import forms

class TaskForm(forms.Form):
    summary = forms.CharField()
    description = forms.CharField()
    slug = forms.CharField()
