from django import forms
from .models import Profile, Image, Comment


class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'post']

    
class PostForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['creator', 'likes', 'time', 'tags', 'comment', 'profile']    

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', ]