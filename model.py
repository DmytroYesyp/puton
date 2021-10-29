from sqlalchemy import create_engine,Column,Integer,String,Enum,ForeignKey
import os
from sqlalchemy import  orm
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
import enum
import sys

sys.path.append(r"/home/lyubomur/PycharmProjects/laab_6")

DB_URI = os.getenv("DB_URI","postgresql://postgres:1462357980@localhost:5432/laab_6")

engine = create_engine(DB_URI)

SessionFactory = sessionmaker(bind=engine)

Session = scoped_session(SessionFactory)

Base = declarative_base()

metadata = Base.metadata
class UserEnum(enum.Enum):

    Lector = 1
    Student = 2

class RequestEnum(enum.Enum):
    OnHold = 1
    Accepted = 2
    Declined = 3



class users(Base):
    __tablename__ = 'users'

    id = Column(Integer,primary_key=True)
    username = Column(String)
    firstName = Column(String)
    lastName = Column(String)
    email = Column(String)
    password = Column(String)
    phone = Column(String)



class course(Base):
    __tablename__ = 'course'

    id = Column(Integer,primary_key=True)
    courseName = Column(String)
    courseDescription = Column(String)



class request(Base):
    __tablename__ = 'request'
    id = Column(Integer, primary_key=True)
    requestFrom = Column(Integer,ForeignKey(users.id))
    requestToCourse = Column(Integer,ForeignKey(course.id))
    requestToLector = Column(Integer,ForeignKey(users.id))

user1 = users(username="username1",firstName="firstname1",lastName="lastName1",email="email1",password="password1",phone="phone1")
user2 = users(username="username2",firstName="firstname2",lastName="lastName2",email="email2",password="password2",phone="phone2")
user3 = users(username="username3",firstName="firstname3",lastName="lastName3",email="email3",password="password3",phone="phone3")
user4 = users(username="username4",firstName="firstname4",lastName="lastName4",email="email4",password="password4",phone="phone4")
user5 = users(username="username5",firstName="firstname5",lastName="lastName5",email="email5",password="password5",phone="phone5")

course1 = course(courseName="courseName1",courseDescription="courseDescription1")
course2 = course(courseName="courseName2",courseDescription="courseDescription2")

request1 = request(requestFrom=1,requestToCourse=1,requestToLector=1)
request2 = request(requestFrom=2,requestToCourse=2,requestToLector=2)


# Session.add(user1)
# Session.add(user2)
# Session.add(user3)
# Session.add(user4)
# Session.add(user5)
# Session.add(course1)
# Session.add(course2)
Session.add(request1)
Session.add(request2)


Session.commit()