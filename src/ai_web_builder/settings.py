import os
from pathlib import Path
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Tải các biến môi trường từ file .env ở thư mục gốc của project
env_path = BASE_DIR.parent / '.env'
load_dotenv(dotenv_path=env_path)

# CHÌA KHÓA BÍ MẬT
SECRET_KEY = os.getenv("SECRET_KEY", "django-insecure-fallback-key-for-development")

# DEBUG MODE
DEBUG = True

ALLOWED_HOSTS = []

# ĐỊNH NGHĨA CÁC APPS
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Apps của chúng ta
    'accounts',
    'generator',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ai_web_builder.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # Thư mục template chung
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

WSGI_APPLICATION = 'ai_web_builder.wsgi.application'

# CẤU HÌNH DATABASE
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR.parent / 'db.sqlite3', # File db ở thư mục gốc
    }
}

# TRÌNH XÁC THỰC MẬT KHẨU
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# QUỐC TẾ HÓA
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# FILE TĨNH (STATIC FILES)
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# KIỂU TRƯỜNG KHÓA CHÍNH MẶC ĐỊNH
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# --- CÁC CÀI ĐẶT CỦA CHÚNG TA ---
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
