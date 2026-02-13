# -*- coding: utf-8 -*-
"""Create the users/urls.py file"""

from __future__ import unicode_literals
from django.conf.urls import url
from django.contrib.auth.views import login
from . import views

urlpatterns = [
    # Login Page
    url(r'^login/$', login, {'template_name': 'users/login.html'}, name = 'login'),
]