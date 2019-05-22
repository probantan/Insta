from django import forms
from .models import Profile, Image, Comment
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()

class PostForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['creator', 'profile','time', 'likes', 'tags']    

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', ]
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields= ['username', 'email']

class ProfileUpdateForm (forms.ModelForm):
    class Meta:
        model= Profile  
        fields=['profile_pic']        