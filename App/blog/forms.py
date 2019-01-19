from blog.models import Profile
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
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


class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
