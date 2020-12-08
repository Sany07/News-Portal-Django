from django import forms
from comment.models import Comment


class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'post',
            'comment',    
            'reply',    
                    
        ]


