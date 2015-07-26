# vim: fileencoding=utf-8 tw=100 expandtab ts=4 sw=4 :
# Django Template Filter that parse a tweet in plain text and turn it with working Urls
# tweet_parser.py
# version : 1.0.0
# License : MIT
# Author : Vincent Loy <vincent.loy1@gmail.com>
# copyright (c) 2015 Vincent Loy

import re

from pytter.pytter import Pytter

from django import template
from django.utils import safestring

register = template.Library()

CUSTOM_CLASSES = {
    'url': 'tweet_url',
    'user': 'tweet_user',
    'hashtag': 'hashtag'
}


@register.filter(name='tweetparser')
def tweetparser(value):
    t = Pytter(value)
    t.set_html_class(CUSTOM_CLASSES)

    return safestring.mark_safe(t.get_html())
