import re

from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)

User = get_user_model()

class LoginForm(forms.Form):
    """
    desc: Form login
    param:    
    """
    username = forms.CharField()
    password = forms.CharField()
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')        
        print("{user} {passwd}".format(user=username, passwd=password))
        if not (username and password):
            # Don't authenticate, just let the other validators handle it.
            return self.cleaned_data
        return self.cleaned_data

