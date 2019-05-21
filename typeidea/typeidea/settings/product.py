from .base import *  # NOQA

DEBUG = False

ALLOWED_HOSTS = ['juedi294.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'typeidea_db',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '172.21.0.8',
        'PORT': 3306,
        'CONN_MAX_AGE': 60,
        'OPTIONS': {'charset': 'utf8mb4'}
    }
}

ADMINS = MANAGERS = (
    ('juedi294', 'juedi294@gmail.com'),  # 你的邮件地址
)

EMAIL_HOST = 'www.849454932@qq.com'
EMAIL_HOST_USER = 'juedi294'
EMAIL_HOST_PASSWORD = 'm15928491249_1'
EMAIL_SUBJECT_PREFIX = 'typeidea'
DEFAULT_FROM_EMAIL = 'wangzhan'
SERVER_EMAIL = 'pop3'

STATIC_ROOT = 'E:\work\programing\typeidea\typeidea_env/static_files/'

REDIS_URL = '127.0.0.1:6379:1'

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': REDIS_URL,
        'TIMEOUT': 300,
        'OPTIONS': {
            # 'PASSWORD': '<对应密码>',
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'PARSER_CLASS': 'redis.connection.HiredisParser',
        },
        'CONNECTION_POOL_CLASS': 'redis.connection.BlockingConnectionPool',
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(levelname)s %(asctime)s %(module)s:'
                      '%(funcName)s:%(lineno)d %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'typeidea.log',
            'formatter': 'default',
            'maxBytes': 1024 * 1024,  # 1M
            'backupCount': 5,
        },

    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
    }
}
