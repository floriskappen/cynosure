
from fastapi import APIRouter
import pytz
import datetime

from entities.event_chains.model import EventChain

router = APIRouter()

@router.post("/ping")
async def ping(event_chain_id: int):

    update_query = EventChain.update(
        last_ping=datetime.datetime.now(pytz.timezone("Europe/Amsterdam")),
        is_closed=False
    ).where(EventChain.id == event_chain_id)
    update_query.execute()
    return { "ok": True }
