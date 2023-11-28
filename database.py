from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,Float,Text,Integer
from datetime import datetime

Base=declarative_base()
class q_and_a(Base):
    __tablename__="Questions_Responses"
    id=Column(Integer,primary_key=True,index=True)
    question=Column(String,index=True)
    answer=Column(String)
    response_time=Column(Float)
    #created_at=Column(DatetTime,default=datetime.utcnow)

engine=create_engine("postgresql://postgres:computer@localhost/chat_completion")

SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

