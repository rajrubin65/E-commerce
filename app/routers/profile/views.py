from fastapi import APIRouter
from app.routers.login.model import CustomerDetails,Loginschema
from app.routers.login.logic import Hasher
from app.routers.profile.model import UserDetails
from configurations.config import ses

hasher = Hasher()
router = APIRouter()

@router.get('/get-user-details')
def get_user_details(id:int):
    user = ses.query(CustomerDetails).filter_by(usershared_id = id).first()
    if user:
        user_details = UserDetails(
            user_name= user.user_name,
            gender= user.gender,
            e_mail= user.e_mail,
            phone= user.phone_no,
            Address= user.Address
        )
        return user_details.dict()
    else:
        return {'message':'user is not valid'}

@router.post('/otp-verification')
def otp_verification():
    pass


@router.post('/change-password')
def change_password(user_name,id,password):
    user = ses.query(Loginschema).filter_by(user_id = id, user_name =user_name).first()
    user.password = hasher.get_password_hash(password)
    return{'message':'password changed sucessfully..'}