#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import patterns, url

from google_product_feeder.views import CSVFeedView


urlpatterns = patterns('google_product_feeder',
    url(r'^google_feed/',
        CSVFeedView.as_view(),
        name='google_feed'),
)
