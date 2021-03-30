import os

DB_CREDENTIALS = {
    'DatabaseHost': os.environ.get('DATABASE_HOST', 'localhost'),
    'DatabaseName': os.environ.get('DATABASE_NAME', 'postgres'),
    'DatabasePort': int(os.environ.get('DATABASE_PORT', '5432')),
    'DatabaseUser': os.environ.get('DATABASE_USER', 'postgres'),
    'DatabasePassword': os.environ.get('DATABASE_PASSWORD', 'root')
}

DB_SCHEMA = ''

DEVELOPMENT_SERVER = 'http://localhost'

REGEX_PARENTHESES = '\\' + '((.*?)' + '\\)'

