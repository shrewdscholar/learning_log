# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import logout

# Create your views here.
def logout_view(request):
    """Logout user"""
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))