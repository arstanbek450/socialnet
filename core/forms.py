from django import forms
from .models import Comment, Short
from django.contrib.auth.models import User

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']


class ShortForm(forms.ModelForm):
    class Meta:
        model = Short
        fields = ['title']


class RegistForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']













