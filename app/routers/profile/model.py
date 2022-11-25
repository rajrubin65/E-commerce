from pydantic import BaseModel


class UserDetails(BaseModel):
    user_name: str
    e_mail :str
    phone :int
    Address :str