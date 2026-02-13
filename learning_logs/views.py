# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Topic
from .forms import TopicForm
# Create your views here.
def index(request):
    """学习笔记的主页"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """Show all of the topics"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request):
    """Show a single topic and all its entries"""
    topic = Topic.object.sget(id = topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    """Show a new page to create new topic"""
    if request.method != 'POST':
        # Unsubmitted data: create a new form
        form = TopicForm()
    else:
        # POST submitted data, process the data
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResonseRedirect(reverse('learning_logs:topic'))
    
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)
