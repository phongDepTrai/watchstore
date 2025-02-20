from django import forms
from mystore.models import User, UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):
    #porfolio = forms.URLField(required = False)
    picture = forms.ImageField(required = False)
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio','picture')