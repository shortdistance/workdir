#!/usr/bin/env python
# coding=utf-8
# vim: set et sw=4 ts=4 sts=4
# Author: YuanLin
# Created: 2015-07-25 12:22 CST

import uuid

# mongodb
MONGODB_SETTINGS = {
    'db': 'qfbot',
    'username': '',
    'password': '',
    'host': '127.0.0.1',
    'port': 27017
}

# redis cache
CACHE_TYPE = 'redis'
CACHE_REDIS_HOST = '127.0.0.1'
CACHE_REDIS_PORT = 6379
CACHE_REDIS_DB = ''
CACHE_REDIS_PASSWORD = ''

#mail sender
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = ''
MAIL_PASSWORD = ''
MAIL_DEFAULT_SENDER = ''

SECURITY_PASSWORD_SALT = uuid.uuid4().get_hex()
SECURITY_PASSWORD_HASH = "bcrypt"
# SECURITY_PASSWORD_HASH = "pbkdf2_sha512"
SECURITY_EMAIL_SENDER = ""

SECURITY_CONFIRM_SALT = uuid.uuid4().get_hex()
SECURITY_REMEMBER_SALT = uuid.uuid4().get_hex()

# Set secret keys for CSRF protection
CSRF_SESSION_KEY = uuid.uuid4().get_hex()

SERVER_EMAIL = ''

# Flask-SocialBlueprint
SOCIAL_BLUEPRINT = {
    # https://github.com/settings/applications/new
    "flask_social_blueprint.providers.Github": {
        # Client ID
        'consumer_key': '6f6…',
        # Client Secret
        'consumer_secret': '1a9…'
    },
}