"""
Django settings for testproject project.

Generated by 'django-admin startproject' using Django 3.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ")uecapso7nzy##1!np4_5^t#+i4@s*7m0d9-&e3-3_gvp2yk9g"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Application definition

ROOT_URLCONF = "test_project.urls"

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django_base_shop",
    "test_shop",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_base_shop.middleware.CartMiddleware",
]


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:",}}

WSGI_APPLICATION = "test_project.wsgi.application"

# Shop Models
SHOP_PRODUCT_MODEL = "test_shop.ConcreteProduct"
SHOP_ORDER_ITEM_MODEL = "test_shop.ConcreteOrderItem"
SHOP_ORDER_MODEL = "test_shop.ConcreteOrder"
SHOP_CART_ITEM_MODEL = "test_shop.ConcreteCartItem"
SHOP_CART_MODEL = "test_shop.ConcreteCart"
SHOP_CHECKOUT_DETAILS_MODEL = "test_shop.ConcreteCheckoutDetails"
