import multiprocessing
from os import environ

bind = environ.get('HOST', '0.0.0.0') + ':' + environ.get('PORT', '8000')
workers = multiprocessing.cpu_count() * 2 + 1
graceful_timeout = 300
reload = True
