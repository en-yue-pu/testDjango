from django import forms

from .models import Comment

class CommentForm(forms.ModelForm):#一个comment包含什么
    class Meta:
        model = Comment
        fields = ["name", "email", "body"]
