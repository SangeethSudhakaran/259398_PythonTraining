from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#define the database
DATABASE_URL = "sqlite:///example.db"
engine = create_engine(DATABASE_URL,echo=True)
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)

#Define a simple ORM model
class User(Base):
    __tablename__ ="users"
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)

#Create databse and Tables
Base.metadata.create_all(engine)

#Create new session
session = SessionLocal()

#Create
new_user = User(name='Sangeeth', age=31)
session.add(new_user)
session.commit()
session.close()