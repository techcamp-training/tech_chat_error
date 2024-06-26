from django import forms
from .models import Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'content', 'name']

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'タイトル', 'rows': 1}),
            'content': forms.Textarea(attrs={'placeholder': '質問内容', 'rows': 3}),
            'name': forms.TextInput(attrs={'placeholder': '投稿者名', 'rows': 1}),
        }