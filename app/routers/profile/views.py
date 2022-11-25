from fastapi import APIRouter
from app.routers.login.model import CustomerDetails
from app.routers.profile.model import UserDetails
from configurations.config import ses


router = APIRouter()

@router.get('/get-user-details')
def get_user_details(name:str):
    user = ses.query(CustomerDetails).filter_by(user_name = name).first()
    user_details = UserDetails(
        user_name= user.user_name,
        e_mail= user.e_mail,
        phone= user.phone_no,
        Address= user.Address
    )
    return user_details.dict()
    