from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    "postgresql://postgres:postgres@localhost:5432/etl", pool_pre_ping=True)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = Session()