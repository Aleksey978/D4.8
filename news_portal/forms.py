from django import forms
from .models import Post, news


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = [
            'title',
            'text',
            'category',
            # 'choose',
            'author'
       ]

