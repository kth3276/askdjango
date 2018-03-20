# dojo/forms.py
# 유저에게 입력 받을 필드만 써준다
from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'user_agent']
        widgets = {
            'user_agent': forms.HiddenInput,
        }



    # '''
    # def save(self, commit=True):
    #     self.instance = Post(**self.cleaned_data)
    #     if commit:
    #         self.instance.save()
    #     return self.instance
    # '''