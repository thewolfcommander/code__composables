"""
Install django-cors-headers

python -m pip install django-cors-headers
"""


# settings.py

INSTALLED_APPS = [
    ...,
    "corsheaders",
    ...,
]

MIDDLEWARE = [
    ...,
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    ...,
]

CORS_ALLOW_ALL_ORIGINS = True

