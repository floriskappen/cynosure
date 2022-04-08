
import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import peewee
import uvicorn
from dotenv import load_dotenv

from entities import entities
from schedules import close_expired_event_chains

load_dotenv()

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Establish a database instance
peewee_db = peewee.PostgresqlDatabase(
    os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
)

# Setup the entities
entities.setup_models(peewee_db)
entities.setup_routes(app)

# Activate schedulers
close_expired_event_chains.schedule()

@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

