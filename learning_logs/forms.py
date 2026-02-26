# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from .models import Topic, Entry
from django import forms

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text', 'public']
        labels = {
            'text': '',
            'public': "Make this topic public?"
            }
        widgets = {
            'public': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}