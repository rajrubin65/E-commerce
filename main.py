import uvicorn
from fastapi import FastAPI
from app.routers.login import views
from app.routers.profile import views as profile_view


app = FastAPI()

app.include_router(views.router)
app.include_router(profile_view.router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=2255,reload= True)