from django import forms
from userManagement.models import Users
from django.contrib.auth.models import User


class registerform(forms.ModelForm):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name','username', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)

        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
            return user


class userform(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['phone', 'gender']