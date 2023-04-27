from sqlalchemy import create_engine, Column, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    deadline = Column(Date)

engine = create_engine('')
Session = sessionmaker(bind=engine)
session = Session()

users = session.query(User).all()
for user in users:
    print(user.id, user.name, user.age)