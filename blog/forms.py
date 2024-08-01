from django import forms

from blog.models import Comment

class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'message', 'rating', 'file']



