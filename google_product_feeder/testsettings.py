MIDDLEWARE_CLASSES = []
ROOT_URLCONF ='google_product_feeder.urls'
DEFAULT_FILE_STORAGE = 'inmemorystorage.InMemoryStorage'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    }
}
SECRET_KEY = 'test'
