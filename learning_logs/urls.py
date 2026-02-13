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

    # Create new topic
    url(r'^new_topic/$', views.new_topic ,name = 'new_topic'),
]