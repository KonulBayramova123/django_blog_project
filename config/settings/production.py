from .base import *

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

DATABASES = {
    'default': env.db()  #takes database_url
}


# Password validation

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

AWS_ACCESS_KEY_ID=env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY=env('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME='blogarticlesapp'
AWS_S3_CUSTOM_DOMAIN='%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS={
   'CacheControl': 'max-age=86400',
}
AWS_LOCATION='static'
STATIC_URL= 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN,AWS_LOCATION)


STORAGES = {
   "default": {
       "BACKEND": "config.storage_backend.MediaStorage",
   },
 
   "staticfiles": {
       "BACKEND": "storages.backends.s3boto3.S3StaticStorage",
   },
}