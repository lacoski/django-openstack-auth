
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r"^login/$", views.login_view, name='login_view'),
    url(r"^logout/$", views.logout_view, name='logout_view'),
    url(r"^log/$", views.log_view, name='log_view'),
    url(r'^login_auth/$', auth_views.login, name='login_auth'),    
]
