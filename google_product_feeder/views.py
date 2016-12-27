#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import View
from django.http import HttpResponse

from google_product_feeder.feed import CSVMerchantFeed, XMLMerchantFeed


class BaseFeedView(View):
    """Base class for Merchant feed views

    Override the ``products`` attribute with a queryset or other iterable of
    products to include in the feed, and the ``feed_class`` attribute with the
    feed class to use.
    """
    def get_products(self):
        """Return an iterable of products to include in the feed"""
        return self.products

    def get_feed_class(self):
        """Return the feed class to use for the feed"""
        return self.feed_class

    def get_feed(self):
        """Return the feed object"""
        feedclass = self.get_feed_class()
        return feedclass(self.get_products())

    def get(self, request):
        """Return a HttpResponse containing the feed data"""
        feed = self.get_feed()
        content = feed.get_content()
        response = HttpResponse(
            content,
            content_type='text/csv',
        )
        response['Content-Disposition'] = 'attachment; filename="google.csv"'
        return response


class CSVFeedView(BaseFeedView):
    """A CSV feed view"""
    products = []
    feed_class = CSVMerchantFeed


class XMLFeedView(BaseFeedView):
    """An XML feed view"""
    products = []
    feed_class = XMLMerchantFeed
