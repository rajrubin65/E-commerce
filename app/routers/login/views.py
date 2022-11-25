from fastapi import APIRouter
from app.routers.login.model import Login,Register
from configurations.config import ses
from app.routers.login.model import Loginschema,CustomerDetails
from app.routers.login.logic import Hasher

router = APIRouter()

hasher = Hasher()



@router.post('/login')
def login(login:Login):
    user = ses.query(Loginschema).filter_by(user_name = login.user_name).first()
    print(user.password)
    if user and hasher.verify_password(login.password, user.password):
        return{'message':"Valid User"}
    else:
        return{'message':"Not a valid user"}


@router.post('/register')
def register_user(register:Register):
    count = ses.query(Loginschema).count()
    reg_user = CustomerDetails(
        user_name = register.user_name,
        e_mail = register.e_mail,
        phone_no = register.phone_no,
        Address = register.address,
        usershared_id = count + 1

    )
    user = Loginschema(
        user_id = count + 1,
        user_name = register.user_name,
        password = hasher.get_password_hash(register.password)
    )

    ses.add(user)
    ses.add(reg_user)
    ses.commit()

    return {'message':"user added successfully..."}