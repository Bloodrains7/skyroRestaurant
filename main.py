from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import init_db
from api import reservations, menu

app = FastAPI()

init_db()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(reservations.router)
app.include_router(menu.router)
