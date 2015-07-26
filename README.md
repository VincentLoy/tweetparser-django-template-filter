# tweetParser Django Template Filter

this is a port of [tweetParser.js](https://github.com/VincentLoy/tweetParser.js) to work as a Django template filter

## How does it work ?
Once installed, just :
```
<p>{{ your_tweet|tweetparser }}</p>
```

## Installation
Set [Pytter](https://github.com/VincentLoy/pytter) as a dependecie of your project in requirements.txt
Or into your virtualenv type :
```console
$ pip install pytter
```

Take a look at the [Django Documentation](https://docs.djangoproject.com/en/1.8/howto/custom-template-tags/)
just create a directory named **templatetags** into your Django app directory and past **tweet_parser.py** into it.
(don't forget to create an empty init file like in the example below)
```console
your_django_app/
    static/
    templates/
    templatetags/
        __init__.py
        tweet_parser.py
    urls.py
    views.py
```

#### then in your template
```htmldjango
{% load tweet_parser %}
<!-- some code -->
<p>{{ your_tweet|tweetparser }}</p>
<!-- some code -->
```

#### You can change the classes given to each anchor tags
```python
USER_CLASS = 'tweet_user'
URL_CLASS = 'tweet_url'
HASHTAG_CLASS = 'hashtag'
```
