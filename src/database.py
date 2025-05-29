from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+pymysql://root:ozcoding_pw@127.0.0.1:33060/ozcoding"

engine = create_engine(DATABASE_URL)

SessionFactory = sessionmaker(
    autocommit=False, autoflush=False, expire_on_commit=False, bind=engine
)
