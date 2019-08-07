from crispy_forms.helper import FormHelper
from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = 'Title'
        self.fields['draft'].label = 'Draft?'
        self.fields['content'].label = 'Content of post'

    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'image',
            'draft',
        ]
