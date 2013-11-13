django-clickbank
=========
[![Build Status](https://travis-ci.org/Sureiya/django-clickbank.png?branch=master)](https://travis-ci.org/Sureiya/django-clickbank) [![Coverage Status](https://coveralls.io/repos/Sureiya/django-clickbank/badge.png?branch=master)](https://coveralls.io/r/Sureiya/django-clickbank?branch=master)

django-clickbank is a pluggable django application for recieving ClickBank [Instant Payment Notifications] [1]

* Recieves and stores all notifications to the database.
* Stores raw post data, whether notifications fails or not (configurable)
* Formats raw CB field names into easier  ones easier to work with.
* Sends signals for each transaction type

django-clickbank is currently written for django 1.5.x and python 2.7, but it should run fine on 1.6.

The only major requirement is that you have South installed.

Installation
--------------
##### Installing with pip from pypi
```sh
pip install django-clickbank
```
##### Installing with pip from github
```sh
pip install -e git+https://github.com/Sureiya/django-clickbank.git
```
##### Manual Installaion
```sh
git clone https://github.com/Sureiya/django-clickbank.git django-clickbank
cd django-clickbank
python setup.py
```

Setup
-------

1. Install (see above)

2. Add django-clickbank and South to your INSTALLED_APPS
```python
# settings.py
INSTALLED_APPS = (
      ...
      'south',
      'django_clickbank',
      ...
)
```

3. Import the django-clickbank default settings in settings.py
```python
    # settings.py
    from django_clickbank.settings import *
```

4. Add django-clickbank urls to your urls.py
```python
urlpatterns = patterns('',
    ...
      url(r'^', include('django_clickbank.urls')),
    ...
)
```

5. Run migrations
```sh
python manage.py migrate django_clickbank
```

6. Setup Clickbank
    1. Login to Clickbank
    2. Navigate to Settings -> My Site
    3. To the right of Advanced Tools, click Edit
    4. Add http://yoursite/clickbank/ipn/ as a URL, you can choose 2.1 or 4.0.
    5. Create a Secret Key
    6. Hit 'Save'

7. Update Settings with Secret Key
```python
# settings.py
CLICKBANK_SECRET_KEY = <key generated in step 6>
```

8. Setup Logging **(Optional)**
```python
# settings.py
LOGGING['loggers']['django_clickbank.notications' = {
    'handlers': ['console'], # Change handlers if you want. Logging levels are DEBUG and INFO
    'propogate': True,
}
```
9. Test it out.

Usage
------
```python
from django_clickbank.signals import sale

def sale_callback(sender, **kwargs):
    ## Logic for processing sale
```
For more information on signals, see [Django Signals] [2]

To view a full list of signals refer to [signals.py] [3]

To view all notification fields, see [models.py] [4]

**Important Note**

Under some circumstances ClickBank sends multiple notifications per sale (upsells). Due to the way Django signals work, its possible for notification callbacks to be processed at the same time (multithreaded server). If your callbacks could fail due to this, look into using a task queue like celergy, along with a single worker to force your callbacks to be executed 'first in first out'.

Available Settings
---------

```
## Setting debug to True turns off things like secret key verification
CLICKBANK_DEBUG = False

## If set to true raw post data will be stored regardless of CLICKBANK_DEBUG
CLICKBANK_STORE_POSTS = True

## If set to true, app will still log notifications when verification fails
CLICKBANK_KEEP_INVALID = True

## When set to true, app will still send signal when invalid notification recieved.
CLICKBANK_SIGNAL_INVALID = False

## Send 200 status when a transaction is received that already exists. Mostly for debugging
CLICKBANK_IGNORE_DUPLICATES = False
```

Contributing
--------------
If you'd like to contribute, feel free to make a fork and send me a pull request.

License
----

MIT
  
[1]: https://support.clickbank.com/entries/22803622-Instant-Notification-Service
[2]: https://docs.djangoproject.com/en/dev/topics/signals/
[3]: https://github.com/Sureiya/django-clickbank/blob/master/django_clickbank/signals.py
[4]: https://github.com/Sureiya/django-clickbank/blob/master/django_clickbank/models.py