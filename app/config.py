import os

SQLALCHEMY_DATABASE_URI = \
    '{engine}://{username}:{password}@{hostname}/{database}'.format(
        engine='mysql',
        username=os.getenv('MYSQL_USER'),
        password=os.getenv('MYSQL_PASSWORD'),
        hostname=os.getenv('MYSQL_HOST'),
        database=os.getenv('MYSQL_DATABASE'))

# set this to false in production
SQLALCHEMY_TRACK_MODIFICATIONS = True
DEBUG = True
