from configparser import SafeConfigParser
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session


config = SafeConfigParser()
config.read("configurations/config.ini")


# MySql_config
MYSQL_HOST = config.get("MYSQLDB", "MYSQL_HOST")
MYSQL_DB = config.get("MYSQLDB", "MYSQL_DB")
MYSQL_USER = config.get("MYSQLDB", "MYSQL_USER_NAME")
MYSQL_PASSWORD = config.get("MYSQLDB", "MYSQL_PASS")
SQLALCHEMY_TRACK_MODIFICATIONS = config.get("MYSQLDB", "SQLALCHEMY_TRACK_MODIFICATIONS")

url = 'mysql://'+ MYSQL_USER +':'+MYSQL_PASSWORD + '@'+ MYSQL_HOST+'/'+MYSQL_DB


db_engine = create_engine(url)
print(db_engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind= db_engine)

with Session(bind=db_engine) as session:
    ses =session


Base = declarative_base()