import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure--r(g^^u220^gba9s!4=od$s)vvw#@n=zo=_8g8-q!ll1qa5esi'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'tinymce',
    'crispy_bootstrap4', 

    'crispy_forms',
    'intern_platform',
    'django_extensions',
]

CRISPY_TEMPLATE_PACK = 'bootstrap4' 

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]

ROOT_URLCONF = 'internplatform.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'internplatform.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Media files (optional, for storing uploaded files)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Email settings
ADMIN_EMAIL = 'jayashreenatrajan7@gmail.com'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_SENDER_NAME='Intern_platform'
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'jayashreenatrajan7@gmail.com'
EMAIL_HOST_PASSWORD = 'glnb uunv zaae zdqd'
DEFAULT_FROM_EMAIL = 'jayashreenatrajan7@gmail.com'
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'


# Custom user model
AUTH_USER_MODEL = 'intern_platform.CustomUser'

SITE_ID = 1


import os

SITE_URL = os.getenv('SITE_URL', 'http://localhost:8000')


TINYMCE_DEFAULT_CONFIG = {
    'custom_undo_redo_levels': 100,
    'selector': 'textarea',
    "menubar": "file edit view insert format tools table help",
    'plugins': 'link image preview codesample contextmenu table code lists fullscreen',
    'toolbar1': 'undo redo | backcolor casechange permanentpen formatpainter removeformat formatselect fontselect fontsizeselect',
    'toolbar2': 'bold italic underline blockquote | alignleft aligncenter alignright alignjustify '
               '| bullist numlist | outdent indent | table | link image | codesample | preview code | tiny_mce_wiris_formulaEditor tiny_mce_wiris_formulaEditorChemistry',
    'contextmenu': 'formats | link image',
    'block_formats': 'Paragraph=p; Header 1=h1; Header 2=h2',
    'fontsize_formats': "8pt 10pt 12pt 14pt 16pt 18pt",
    'content_style': "body { font-family: Arial; background: white; color: black; font-size: 12pt}",
    'codesample_languages': [
        {'text': 'Python', 'value': 'python'}, {'text': 'HTML/XML', 'value': 'markup'},],
    'image_class_list': [{'title': 'Fluid', 'value': 'img-fluid', 'style': {} }],
    'width': 'auto',
    "height": "600px",
    'image_caption': True,
}