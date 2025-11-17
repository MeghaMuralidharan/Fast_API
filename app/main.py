from fastapi import FastAPI
from app.routes import register,login
# Correct import
from app.routes.user_routes import router as user_router 

app = FastAPI()

app.include_router(register.router)
app.include_router(login.router)
app.include_router(user_router)

@app.get('/')
def index():
    return {'Message':'Hello World!'}