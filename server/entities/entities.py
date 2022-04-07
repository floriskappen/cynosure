
from typing import List

import peewee
from peewee import PostgresqlDatabase
from fastapi import FastAPI

from entities.events.model import Event
from entities.events.router import router as event_router
from entities.domains.model import Domain
from entities.sessions.model import Session
from entities.event_chains.model import EventChain

models: List[peewee.Model] = [Domain, Session, EventChain, Event]

def setup_models(peewee_db: PostgresqlDatabase):
    peewee_db.connect()
    for model in models:
        model.bind(peewee_db)
        if not model.table_exists():
            model.create_table()


def setup_routes(app: FastAPI):
    app.include_router(
        event_router,
        prefix="/events"
    )
