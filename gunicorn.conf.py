from os import environ

bind = environ.get('HOST', '0.0.0.0') + ':' + environ.get('PORT', '8080')
workers = environ.get('WORKERS', 8)
graceful_timeout = 300
