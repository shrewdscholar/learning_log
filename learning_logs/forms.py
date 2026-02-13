# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from .models import Topic

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}