from django import forms
from .models import User
class UserLoginForm(forms.Form):
    email = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


 
# create a ModelForm
class UserCreationForm(forms.ModelForm):
    
    class Meta:
        model = User
        exclude = ['is_active','is_admin','last_login']
        fields=['name','email','phone_number','password']