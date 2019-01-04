from django import forms


class UpdateProfileForm(forms.Form):
    # username=forms.CharField(max_length=20,label='Username on this site')
    dc_username = forms.CharField(max_length=40, label='Username on DC++')
    name = forms.CharField(max_length=250, label='Name (optional)')
    something = forms.CharField(max_length=300)


class CommentForm(forms.Form):
    comment = forms.CharField(max_length=250, label="Comment")
