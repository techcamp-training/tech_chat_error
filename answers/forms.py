from django import forms
from .models import Answer

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['name']

        widgets = {
            'content': forms.Textarea(attrs={'placeholder': '回答する', 'rows': 3}),
            'name': forms.TextInput(attrs={'placeholder': '投稿者名', 'rows': 1}),
        }