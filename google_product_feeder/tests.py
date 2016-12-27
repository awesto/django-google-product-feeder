#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.core.urlresolvers import reverse

from google_product_feeder.feed import CSVMerchantFeed, MERCHANT_FEED_COLUMNS


CSV_HEADINGS = ','.join(MERCHANT_FEED_COLUMNS) + '\r\n'


class AttrNameFakeModel(object):
    # A fake model that returns the attribute name upon attribute access.
    def __getattr__(self, name):
        return name


class EmptyFakeModel(object):
    # A fake model with no attributes.
    def __getattr__(self, name):
        raise AttributeError


class UppercaseBrandFeed(CSVMerchantFeed):
    def get_brand(self, obj):
        return obj.brand.upper()


class CSVMerchantFeedTest(TestCase):

    def test_csv_empty(self):
        feed = CSVMerchantFeed([])
        output = feed.get_content()
        self.assertEquals(output, CSV_HEADINGS)

    def test_csv(self):
        feed = CSVMerchantFeed([AttrNameFakeModel()])
        output = feed.get_content()
        self.assertEquals(output, CSV_HEADINGS * 2)

    def test_csv_missing_attribute(self):
        feed = CSVMerchantFeed([EmptyFakeModel()])
        output = feed.get_content()
        empty_data_row = ',' * (len(MERCHANT_FEED_COLUMNS) - 1) + '\r\n'
        self.assertEquals(output, CSV_HEADINGS + empty_data_row)

    def test_csv_with_get_method(self):
        feed = UppercaseBrandFeed([AttrNameFakeModel()])
        output = feed.get_content()
        data_row = CSV_HEADINGS.replace('brand', 'BRAND')
        self.assertEquals(output, CSV_HEADINGS + data_row)


class CSVFeedViewTest(TestCase):

    def test_view_empty(self):
        url = reverse('google_feed')
        response = self.client.get(url)
        self.assertEquals(response.content, CSV_HEADINGS)

    def test_has_correct_headers(self):
        # content-type is 'text/csv', content-disposition is 'attachment',
        # filename is 'google.csv'
        url = reverse('google_feed')
        response = self.client.get(url)
        self.assertEqual(response['Content-Type'],
                         'text/csv')
        self.assertEqual(response['Content-Disposition'],
                         'attachment; filename="google.csv"')
