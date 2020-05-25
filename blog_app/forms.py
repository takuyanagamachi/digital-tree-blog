from django import forms
from .models import Post, Tag, Comment
from django.forms import ModelForm

class PostAddForm(forms.ModelForm):    
    class Meta:
        model = Post
        fields = ['title', 'text', 'image', 'tag']

class CmtForm(forms.ModelForm):    
    class Meta:
        model = Comment
        fields = ['text']
class ContactForm(forms.Form):
    name = forms.CharField(label='お名前', max_length=50)
    email = forms.EmailField(label='メールアドレス',)
    message = forms.CharField(label='メッセージ', widget=forms.Textarea)
    myself = forms.BooleanField(label='内容を受け取る', required=False)