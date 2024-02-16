import os

APP_ENV = os.getenv('APP_ENV', 'development')
DATABASE_USERNAME = os.getenv('DATABASE_USERNAME', 'muntasir')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD', 'Siyam529')
DATABASE_HOST = os.getenv('DATABASE_HOST', 'localhost')
DATABASE_NAME = os.getenv('DATABASE_NAME', 'week-to-do')
TEST_DATABASE_NAME = os.getenv('DATABASE_NAME', 'test-week-to-do')
