from blog.models import Profile
from django import forms
from django.forms import ModelForm


class UpdateProfileForm(ModelForm):
    # username=forms.CharField(max_length=20,label='Username on this site')
    # dc_username = forms.CharField(max_length=40, label='Username on DC++')
    # name = forms.CharField(max_length=250, label='Name (optional)')
    # something = forms.CharField(max_length=300)
    # profile_picture=forms.ImageField(upload_to='images/%Y/%m/%d/')
    class Meta:
        model = Profile
        fields = ['dc_username', 'something', 'profile_picture']


class CommentForm(forms.Form):
    comment = forms.CharField(max_length=250, label="Comment")
