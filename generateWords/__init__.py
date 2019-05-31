import pymysql
from config.database import DATABASE

db = pymysql.connect(
    DATABASE['host'],
    DATABASE['user'],
    DATABASE['password'],
    DATABASE['database']
)