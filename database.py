from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://root:root@localhost/stock"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, echo=True, future=True
)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()

# import psycopg2
# conn = psycopg2.connect(database="kafka-test", user='root', password='root', host='127.0.0.1', port= '5432')
# cursor = conn.cursor()

# cursor.execute("DROP TABLE IF EXISTS Station_Status")
# sql ='''CREATE TABLE Station_Status(
#     Station_id CHAR(20) NOT NULL,
#     is_installed INT,
#     is_renting INT,
#     is_returning INT,
#     last_reported INT,
#     num_bikes_available INT,
#     num_docks_available INT,
#     date timestamp
# )'''
# cursor.execute(sql)
# conn.commit()

# conn.close()