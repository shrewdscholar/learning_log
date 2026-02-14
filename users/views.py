# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def logout_view(request):
    """Logout user"""
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))

def regitser(request):
    """Register new user"""
    if request.method != 'POST':
        # Display an empty registration form
        form = UserCreationForm()
    else:
        # Process the completed form
        form = UserCreationForm(data = request.POST)
        if form.is_valid():
            new_user = form.save()
            # Log the user in automatically and redirect to home
            authenticated_user = authenticate(username = new_user.username, password = request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))
    context = {'form': form}
    return render(request, 'users/register.html', context)