# vim: fileencoding=utf-8 tw=100 expandtab ts=4 sw=4 :
# Django Template Filter that parse a tweet in plain text and turn it with working Urls
# tweet_parser.py
# version : 1.0.0
# License : MIT
# Author : Vincent Loy <vincent.loy1@gmail.com>
# copyright (c) 2015 Vincent Loy

import re

from django import template
from django.utils import safestring

register = template.Library()

USER_CLASS = 'tweet_user'
URL_CLASS = 'tweet_url'
HASHTAG_CLASS = 'hashtag'


@register.filter(name='tweetparser')
def tweetparser(value):
    def parse_url(tweet):
        url_regex = '(^|\s)((f|ht)tps?://([^ \t\r\n]*[^ \t\r\n\)*_,\.]))'
        match = re.findall(url_regex, value)

        if match:
            for m in match:
                link = '<a href="{url}" target="_blank" class="{tweetclass}">{text}</a>' \
                    .format(url=m[1], text=m[1], tweetclass=URL_CLASS)
                tweet = tweet.replace(m[1], link)

            return tweet

    def parse_users(tweet):
        user_regex = '(\B@([a-zA-Z0-9_]+))'
        match = re.findall(user_regex, tweet)

        if match:
            for m in match:
                base_url = 'https://twitter.com/'
                link = '<a href="{base_url}{user_only}" target="_blank" class="{tweetclass}">{text}</a>' \
                    .format(base_url=base_url, user_only=m[1], text=m[0], tweetclass=USER_CLASS)

                tweet = tweet.replace(m[0], link)

        return tweet

    def parse_hashtags(tweet):
        hashtag_regex = '(\B#([á-úÁ-Úä-üÄ-Üa-zA-Z0-9_]+))'

        match = re.findall(hashtag_regex, tweet)

        if match:
            for m in match:
                base_url = 'https://twitter.com/hashtag/'
                link = '<a href="{base_url}{hashtag_text}" target="_blank" class="{tweetclass}">{hashtag}</a>' \
                    .format(base_url=base_url, hashtag_text=m[1], hashtag=m[0], tweetclass=HASHTAG_CLASS)

                tweet = tweet.replace(m[0], link)

        return tweet

    value = parse_url(value)
    value = parse_users(value)
    value = parse_hashtags(value)

    return safestring.mark_safe(value)