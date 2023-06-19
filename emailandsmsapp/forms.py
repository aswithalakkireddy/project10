from django import forms
class RegForm(forms.Form):
    FirstName=forms.CharField(max_length=10)
    LastName=forms.CharField(max_length=10)
    UserName=forms.CharField(max_length=10)
    password=forms.CharField(max_length=10,widget=forms.PasswordInput())
    cpassword=forms.CharField(max_length=10,widget=forms.PasswordInput())
    Emailid=forms.EmailField()
    MoblieNo=forms.CharField(max_length=13)