# -*- coding: utf-8 -*-
"""Create the learning_logs/urls.py file"""

from __future__ import unicode_literals
from django.conf.urls import url
from . import views

urlpatterns = [
    # Home page
    url(r'^$', views.index, name = 'index'),
]
