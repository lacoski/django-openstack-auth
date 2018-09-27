# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)

from django.contrib.auth.models import (
    User
)

from openstack_auth import user as auth_user
from openstack_auth import exceptions

import json

from .forms import (
    LoginForm,
)
# Create your views here.

def login_view(request):
    """
    Đăng nhập
    """
    print('------------------')
    if request.user.is_authenticated:
        print('Session is authenticate')
    for key, value in request.session.items():
            print('{} => {}'.format(key, value))

    print('Check value')
    print(request.user.is_authenticated)
    print('------------------')
    form = LoginForm(request.POST or None)    
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get('password')
        try:
            user = authenticate(username=username, password=password)
            #print(user)
            #json.dumps(user.token)
            auth_user.set_session_from_user(request, user)
        except exceptions.KeystoneAuthException as exc:
            print('Login fail')
            
    return render(request, 'authentication/login.html')
