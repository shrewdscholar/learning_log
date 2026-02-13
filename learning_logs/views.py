# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
# Create your views here.
def index(request):
    """学习笔记的主页"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """Show all of the topics"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request,topic_id):
    """Show a single topic and all its entries"""
    topic = Topic.objects.get(id = topic_id)
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
            return HttpResponseRedirect(reverse('learning_logs:topics'))
    
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

def new_entry(request,topic_id):
    """Create a new entry"""
    print("接收到的 topic_id 是:", topic_id)  # ← 加这行
    print("topic_id 的类型是:", type(topic_id))  # ← 加这行
    topic = Topic.objects.get(id = topic_id)
    if request.method != 'POST':
        # Unsubmitted data: create a new form
        form = EntryForm()
    else:
        # POST submitted data, process the data
        form = EntryForm(request.POST)
        if form.is_valid():
            new_entry = form.save(commit = False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args = [topic_id]))
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

def edit_entry(request,entry_id):
    """Edit your entry"""
    entry = Entry.objects.get(id = entry_id)
    topic = entry.topic
    if request.method != 'POST':
        # pre-populate form with existing entry
        form = EntryForm(instance = entry)
    else:
        # POST submitted data,process the data
        form = EntryForm(instance = entry,data = request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',args = [topic.id]))
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)