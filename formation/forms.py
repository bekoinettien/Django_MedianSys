from django import forms


class SignupForm(forms.Form):
    Prenoms = forms.CharField(max_length=25, required=True)
    Nom = forms.CharField(max_length=15,required=True)
    Email = forms.EmailField(max_length=50, required=True)
    password = forms.CharField(min_length=6,required=True, widget=forms.PasswordInput())
    condition = forms.BooleanField(initial=True)
