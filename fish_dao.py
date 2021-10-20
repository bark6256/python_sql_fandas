# pip install numpy
# pip install pandas
# python -m pip install 머시기

# 마리아디비 연결하는 법 - sqlalchemy
# https://mariadb.com/ko/resources/blog/using-sqlalchemy-with-mariadb-connector-python-part-1/

# pandas 라이브러리로 insert, select 하는 법 (sqlalchemy의 engine(connection) 필요)
# https://ayoteralab.tistory.com/entry/AT-09-mariadbmysql-connection-with-python-2

# session 객체 만들어서 orm 사용하는 법 (파이썬 클래스로 질의)
# https://docs.sqlalchemy.org/en/14/orm/tutorial.html#creating-a-session

# 이스케이프 문자 (\n)

import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from pandas.io import sql
import sqlalchemy as db

from data.fish_api import getFishData
from sqlalchemy.orm import sessionmaker

# dict 타입으로 insert하고 dict타입으로 select하는게 가장 편하다.
# - pymysql 라이브러리 (mysql, mariadb)
# DataFrame도 DB에 insert, select가 가능하다.
# - SQLAlchemy (ORM)
# class타입으로도 insert, select가 가능하다.

engine = db.create_engine("mariadb+mariadbconnector://python:python1234@127.0.0.1:3306/pythondb")
Session = sessionmaker(bind=engine)
session = Session()

def insert():
    fishs = getFishData()
    fishs.to_sql("fish",engine,index=False, if_exists="replace")

def select():
    df = pd.read_sql(con=engine, sql="select * from fish")
    print(df)



#insert()
select()