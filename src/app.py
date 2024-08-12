import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = ["http://localhost:8080"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# TODO : differentiate public & protected Api's
# app.include_router(user_profile.router, prefix="/user", tags=['User Data'])
# app.include_router(login.router, prefix="/login", tags=['Login Authentication'])
# app.include_router(logout.router, prefix="/logout", tags=['Logout'])

@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == '__main__':
    uvicorn.run("app:app", host='127.0.0.1', port=8080, log_level="info", reload=True)
