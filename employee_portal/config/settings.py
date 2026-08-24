INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'employees',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'employeedb',
        'USER': 'employeeuser',
        'PASSWORD': 'StrongPassword123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_DIRS = [
    BASE_DIR / "static"
]

ALLOWED_HOSTS = [
    '*'
]

~

