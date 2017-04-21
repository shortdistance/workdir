# Scrapy settings for crawl project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

import uuid
import os
import sys

BOT_NAME = 'crawl'

SPIDER_MODULES = ['crawl.spiders']
NEWSPIDER_MODULE = 'crawl.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'crawl (+http://www.yourdomain.com)'

MONGO_URI = 'mongodb://localhost:27017/'
MONGO_DB = 'qfbot'
REDIS_URI = 'redis://localhost:6379/1'



COOKIE_STR = uuid.uuid4().get_hex()

DEBUG = False

STATIC = os.path.join(os.path.abspath(__file__), 'static')
TEMPLATE = os.path.join(os.path.abspath(__file__), 'templates')

MAX_CONTENT_LENGTH = 16 * 1024 * 1024

# available languages
LANGUAGES = {
    'en': 'English',
    'zh': 'Chinese'
}

BABEL_DEFAULT_LOCALE = 'zh'

GRAVATAR_BASE_URL = 'http://www.gravatar.com/avatar/'
DEAFULT_AVATAR = 'your default avatar'

LOGIN_DISABLED = False
SECURITY_CONFIRMABLE = True
SECURITY_REGISTERABLE = True
SECURITY_RECOVERABLE = True
SECURITY_CHANGEABLE = True
SECURITY_DEFAULT_REMEMBER_ME = True
CSRF_ENABLED = True
SECURITY_LOGIN_URL = '/security/login'
SECURITY_REGISTER_URL = '/security/register'

try:
    from .conf.develop import *
except ImportError:
    print('You need rename local_config.py.example to local_config.py, '
          'then update your settings')
    raise