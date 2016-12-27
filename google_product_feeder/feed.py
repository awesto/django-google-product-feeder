#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import StringIO
import csv


MERCHANT_FEED_COLUMNS = [
    'id',
    'title',
    'description',
    'google_product_category',
    'product_type',
    'link',
    'mobile_link',
    'image_link',
    'additional_image_link',
    'condition',
    'availability',
    'availability_date',
    'price',
    'sale_price',
    'sale_price_effective_date',
    'brand',
    'gtin',
    'mpn',
    'identifier_exists',
    'shipping',
]


class BaseMerchantFeed(object):
    """A Google Merchant Feed

    When instantiating the feed, pass an iterable of products as the only
    argument.
    The feed will look for attributes on the products that match the attribute
    names defined by the Google feed specification. Subclasses can implement
    get_* methods that match the attribute names to customize this behaviour. A
    get_* method on the subclass will take precedence over an attribute on the
    product. get_* methods are passed the product being processed as their only
    argument. If neither a get_* method nor an attribute on the product are
    found, an empty value will be used for that attribute.
    """
    def __init__(self, objects):
        self.objects = objects

    def _get_column(self, obj, column):
        method_name = "get_%s" % column
        try:
            method = getattr(self, method_name)
        except AttributeError:
            pass
        else:
            return method(obj)
        try:
            attribute = getattr(obj, column)
        except AttributeError:
            pass
        else:
            return attribute
        return ""

    def get_content(self):
        raise NotImplementedError  # pragma: nocover


class CSVMerchantFeed(BaseMerchantFeed):

    def get_content(self):
        rows = [MERCHANT_FEED_COLUMNS]
        for obj in self.objects:
            rows.append([
                self._get_column(obj, col).encode('utf-8')
                for col in MERCHANT_FEED_COLUMNS
            ])
        output = StringIO.StringIO()
        writer = csv.writer(output)
        writer.writerows(rows)
        return output.getvalue()


class XMLMerchantFeed(BaseMerchantFeed):

    def get_content(self):
        raise NotImplementedError  # pragma: nocover
