"""
Django settings for worklog project.

Generated by 'django-admin startproject' using Django 5.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv
from decouple import config

SECRET_KEY = config('SECRET_KEY', default='fallback_secret_key')
BASE_URL = config('BASE_URL', default='http://localhost:8000')
REACT_APP_BASE_URL = config('REACT_APP_BASE_URL', default='http://localhost:8000/login/redirect')

# Build paths inside the project like this: BASE_DIR / 'subdir'.
#Base directory == worklog/backend/worklog
BASE_DIR = Path(__file__).resolve().parent.parent


dotenv_path = BASE_DIR.parent / '.env'
load_dotenv(dotenv_path)

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")
AWS_REGION_NAME = os.getenv("AWS_REGION_NAME")
AWS_SIGNATURE_VERSION = os.getenv("AWS_SIGNATURE_VERSION")

#POSTGRESQL data
POSTGRESQL_USER = os.getenv("POSTGRESQL_USER")
POSTGRESQL_PASSWORD = os.getenv("POSTGRESQL_PASSWORD")
POSTGRESQL_DB_NAME = os.getenv("POSTGRESQL_DB_NAME")
POSTGRESQL_PORT = os.getenv("POSTGRESQL_PORT")
POSTGRESQL_HOST = os.getenv("POSTGRESQL_HOST")


AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_REGION_NAME}.amazonaws.com"
AWS_LOCATION = 'media'
#gpt key를 환경변수로 설정
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/"
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
MEDIA_URL = '/media/'  # 이 URL을 통해 미디어 파일에 접근
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # 파일이 저장될 경로




# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# ALLOWED_HOSTS = [
#     "localhost",
#     "127.0.0.1",
#     "[::1]",
#     "www.dot-worklog.com",
#     "dot-worklog.com",
#     "api.dot-worklog.com",
#     "15.164.56.168",
#     ".ap-northeast-2.compute.amazonaws.com",
# ]

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "15.164.56.168",
]

# CORS
CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOWED_ORIGINS = [

]
# CORS_ALLOW_CREDENTIALS = True
# CORS_ALLOW_HEADERS = '*'

# CSRF
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    'http://localhost:8000',
    'http://127.0.0.1:8000',
    "https://dot-worklog.com",
    "https://www.dot-worklog.com",
    "http://15.164.56.168", 
    "http://ec2-43-202-115-16.ap-northeast-2.compute.amazonaws.com"
    ]

CSRF_COOKIE_NAME = "csrftoken"
CSRF_COOKIE_SAMESITE = 'Lax'
CSRF_COOKIE_SECURE = True

CSRF_COOKIE_HTTPONLY = False

SESSION_COOKIE_SECURE = True
SESSION_COOKIE_SAMESITE = 'Lax'

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    # Auth Settings
    
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.kakao",
    "allauth.socialaccount.providers.google",
    "dj_rest_auth",
    "dj_rest_auth.registration",
    "rest_framework.authtoken",
        
    "rest_framework",
    "corsheaders",
    "profiles",
    
    # s3 저장
    'storages',

]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    # "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    # "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    
    'allauth.account.middleware.AccountMiddleware', 
]
SESSION_ENGINE = 'django.contrib.sessions.backends.db'

ROOT_URLCONF = "worklog.urls"

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

WSGI_APPLICATION = "worklog.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": POSTGRESQL_DB_NAME,
        "USER": POSTGRESQL_USER,
        "PASSWORD": POSTGRESQL_PASSWORD,
        "HOST": POSTGRESQL_HOST,
        "PORT": POSTGRESQL_PORT,
        
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators


AUTH_USER_MODEL = 'profiles.User'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

SITE_ID = 1

# account

ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_AUTHENTICATION_METHOD = 'username'
ACCOUNT_EMAIL_REQUIRED = False
ACCOUNT_USERNAME_REQUIRED = True



REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        # 'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}

REST_AUTH_REGISTER_SERIALIZERS = {
    'REGISTER_SERIALIZER': 'profiles.serializers.UserRegisterSerializer',
}

REST_USE_JWT = True     #JSON Web Token을 사용하겠다는 설정

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Seoul"

USE_I18N = True

USE_TZ = True




# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "/static/"

STATICFILES_DIRS = [BASE_DIR, 'static']

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,  # 기존 로거 비활성화 여부
    'formatters': {  # 로그 메시지 형식 정의
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {  # 로그 메시지 처리 방법 정의
        'console': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',  # 사용할 포맷터
        },
    },
    'loggers': {  # 특정 로거 설정
        'django': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}