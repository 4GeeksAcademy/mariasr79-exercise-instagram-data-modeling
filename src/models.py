import os
import sys
import sqlalchemy
import eralchemy2
from sqlalchemy import Column, ForeignKey, Integer, String, Enum # type: ignore
from sqlalchemy.orm import relationship, declarative_base # type: ignore
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine # type: ignore
from eralchemy2 import render_er # type: ignore

Base = declarative_base()

class User(Base):
     __tablename__ = 'user'
     Id = Column(Integer, primary_key = True)
     UserName = Column(String(20), nullable = False, unique = True)
     Email = Column(String(20), nullable = False, unique = True)

class Follower(Base):
     __tablename__ = 'follower'
     Id = Column(Integer, primary_key= True)
     UserFromId = Column(Integer, ForeignKey("user.Id"))
     UserToId = Column(Integer, ForeignKey("user.Id"))
     UserFrom = relationship("User", foreign_keys=[UserFromId])
     UserTo = relationship("User", foreign_keys=[UserToId])

class Media(Base):
     __tablename__ = 'media'
     Id = Column(Integer, primary_key = True)
     Type = Column(Enum('image', 'video', 'audio', name='media_types'))
     Url = Column(String(20), nullable = False, unique = True)
     PostId = Column(Integer,ForeignKey("post.Id"))   

class Post(Base):
     __tablename__ = 'post'
     Id = Column(Integer, primary_key= True)
     UserId = Column(Integer, ForeignKey("user.Id"))
     User = relationship("User")
     Media = relationship("Media", backref="post")
     

class Comment(Base):
     __tablename__ = 'comment'
     Id = Column(Integer, primary_key= True)
     CommentText = Column(String(20), nullable = False, unique = True)
     AuthorId = Column(Integer, ForeignKey("user.Id"))
     PostId = Column(Integer,ForeignKey("post.Id")) 
     Post = relationship("Post")
     User = relationship("User")




## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
