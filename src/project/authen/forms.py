import re

from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model,
)
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.debug import sensitive_variables
from django.contrib.auth import forms as django_auth_forms


User = get_user_model()
from openstack_auth import exceptions
from openstack_auth import utils

LOG = logging.getLogger(__name__)

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