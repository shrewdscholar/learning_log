# -*- coding: utf-8 -*-
"""Create the learning_logs/urls.py file"""

from __future__ import unicode_literals
from django.conf.urls import url
from . import views

urlpatterns = [
    # Home page
    url(r'^$', views.index, name = 'index'),

    # Show all of the topics
    url(r'^topics/$', views.topics, name = 'topics'),

    # Show entries of topic
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name = 'topic'),

    # Add new topic
    url(r'^new_topic/$', views.new_topic ,name = 'new_topic'),

    # Add new entry
    url(r'^topics/(?P<topic_id>\d+)/new_entry/$', views.new_entry, name='new_entry'),

    # Edit entry
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name = 'edit_entry'),
]