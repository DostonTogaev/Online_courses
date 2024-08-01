from django import forms

from courses.models import Comment

class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'message', 'rating', 'file']



