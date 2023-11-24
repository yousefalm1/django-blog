from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment  # Corrected from 'Model' to 'model'
        fields = ('body',)
