from django import forms
from .models import Post, Tag
from django.forms import ModelForm

class PostAddForm(forms.ModelForm):    
    class Meta:
        model = Post
        fields = ['title', 'text', 'image', 'tag']

class ContactForm(forms.Form):
    subject = forms.CharField(label='お名前', max_length=50)
    sender = forms.EmailField(label='メールアドレス',)
    message = forms.CharField(label='メッセージ', widget=forms.Textarea)
    myself = forms.BooleanField(label='確認内容を受け取る', required=False)