# ProjectDiaDanh/settings.py

from pathlib import Path
from decouple import config
import dj_database_url # Cần thiết để xử lý Database URL
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# =================================================================
# CẤU HÌNH CƠ BẢN VÀ BẢO MẬT
# =================================================================

# Đọc SECRET_KEY từ biến môi trường (an toàn hơn)
SECRET_KEY = config('SECRET_KEY', default='django-insecure-j6%i9e*s_0(f=e2g1g5(x+7y51h^1k2k52j*6j4l6h3e')

# Đọc DEBUG từ biến môi trường. Mặc định là False khi deploy; True khi trên PC
# --- CẤU HÌNH DEBUG TỰ ĐỘNG ---
# Kiểm tra xem có đang chạy trên Render không?
if 'RENDER' in os.environ:
    # Đang trên Render -> Bắt buộc tắt Debug để bảo mật
    DEBUG = False
    print("--- MÔI TRƯỜNG: PRODUCTION (Render) ---")
else:
    # Không có biến RENDER -> Đang ở máy tính cá nhân -> Bật Debug
    DEBUG = True
    print("--- MÔI TRƯỜNG: LOCAL (Development) ---")

if DEBUG:
    ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '*']
else:
    # --- THAY 'TEN_MIEN_CUA_BAN.com' BẰNG TÊN MIỀN CỦA BẠN ---
    CUSTOM_DOMAIN = 'diadiem.lenamvn.com'
    
    ALLOWED_HOSTS = [
        config('WEB_HOST', default=''), # Tên miền Render (diadiem-1.onrender.com)
        '.onrender.com',               # Cho phép các sub-domain của Render
        CUSTOM_DOMAIN,                 # Tên miền gốc (ví dụ: mydiadiem.com)
        f'www.{CUSTOM_DOMAIN}',        # Tên miền có www (ví dụ: www.mydiadiem.com)
    ]
    
# ...

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Ứng dụng bên thứ ba
    'rest_framework',
    'cloudinary',
    'cloudinary_storage',
    
    # Ứng dụng của bạn
    'locations',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # <-- THÊM CHO STATIC FILE KHI DEPLOY
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ProjectDiaDanh.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'ProjectDiaDanh.wsgi.application'

# =================================================================
# DATABASE (SQLite cho Dev, PostgreSQL cho Prod)
# =================================================================

if DEBUG:
    # Dùng SQLite cho môi trường phát triển cục bộ
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    # Dùng PostgreSQL cho môi trường Render (Production)
    DATABASES = {
        'default': dj_database_url.config(
            default=config('DATABASE_URL')
        )
    }

# Password validation (giữ nguyên)
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# =================================================================
# STATIC FILES VÀ MEDIA (Cloudinary & WhiteNoise)
# =================================================================

# 1. Cấu hình Static files (CSS, JS)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles' # Nơi WhiteNoise thu thập Static files
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage' # Cấu hình WhiteNoise

# 2. Cấu hình Media files (Hình ảnh)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# 3. Cấu hình Cloudinary
# CLOUDINARY_STORAGE = {
#    'CLOUD_NAME': config('CLOUDINARY_CLOUD_NAME'),
#    'API_KEY': config('CLOUDINARY_API_KEY'),
#    'API_SECRET': config('CLOUDINARY_API_SECRET'),
# ==============================================================================
# CẤU HÌNH STORAGE CHO DJANGO 5.x (BẮT BUỘC)
# ==============================================================================

# Đảm bảo thư viện Cloudinary đã được import cấu hình
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': config('CLOUDINARY_CLOUD_NAME'),
    'API_KEY': config('CLOUDINARY_API_KEY'),
    'API_SECRET': config('CLOUDINARY_API_SECRET'),
}

# Cấu hình STORAGES mới thay thế cho DEFAULT_FILE_STORAGE cũ
STORAGES = {
    # 1. Quản lý Media (Ảnh upload lên Cloudinary)
    "default": {
        "BACKEND": "cloudinary_storage.storage.MediaCloudinaryStorage",
    },
    # 2. Quản lý Static files (CSS/JS dùng WhiteNoise)
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# Đặt Cloudinary làm nơi lưu trữ mặc định cho MEDIA (files upload)
# DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
