from django import forms
from first.models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        widgets = {
            'comment': forms.TextInput(attrs={
                'id':'comment-text',
                'required': True,
                'placeholder':"Ваш комментарий"
                }),
        }
