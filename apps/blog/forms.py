from django import forms

from apps.blog.models import Post

class PosCreateForms(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')