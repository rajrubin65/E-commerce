from pydantic import BaseModel
from configurations.config import Base,db_engine
from sqlalchemy.schema import Column
from sqlalchemy.types import *
from sqlalchemy.orm import relationship
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String


class Loginschema(Base):
    __tablename__ = 'customers'
    user_id = Column("USER_ID",Integer,nullable=False,primary_key= True)
    user_name = Column("USER_NAME",String(20))
    password = Column("PASSWORD",String(255))

    field_data = relationship("CustomerDetails", backref = "node",uselist = False)

class CustomerDetails(Base):
    __tablename__ = 'customer_details'
    customer_id = Column("CUSTOMER_ID",Integer,primary_key= True, nullable= False)
    user_name = Column("USER_NAME",String(20))
    e_mail = Column("EMAIL",String(20))
    phone_no = Column("PHONE_NUMBER",BigInteger)
    Address = Column("ADDRESS",Text(500))
    usershared_id = Column("USER_SHARED_ID",Integer, ForeignKey(Loginschema.user_id))


Base.metadata.create_all(bind=db_engine)


class Login(BaseModel):
    user_name :str
    password :str


class Register(BaseModel):
    user_name :str
    e_mail :str
    phone_no :int
    address :str
    password: str