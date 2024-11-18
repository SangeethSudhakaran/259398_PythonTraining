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
new_user = User(name='Sam', age=27)
session.add(new_user)
session.commit()

#Read
users = session.query(User).all()
print("All Users")
print("------------------------------------------")
for user in users:
    print("UserID",user.id,"\tName",user.name,"\tAge",user.age)
    print("------------------------------------------")

# Update
user_to_update = session.query(User).filter_by(id=2).first()
if(user_to_update):
    user_to_update.age=27
    user_to_update.name='Sam'
    session.commit()    

# Delete
user_to_delete = session.query(User).filter_by(id=2).first()
if(user_to_delete):
    session.delete(user_to_delete)
    session.commit()    

#End session    
session.close()