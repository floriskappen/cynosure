
import datetime
from tldextract import tldextract

from fastapi import APIRouter
from pydantic import BaseModel

from entities.events.model import Event
from entities.sessions.model import Session
from entities.domains.model import Domain
from entities.paths.model import Path

router = APIRouter()

class EventCreateRequest(BaseModel):
    url: str
    duration: int

@router.post("")
async def create(event_create_request: EventCreateRequest):
    extracted = tldextract.extract(event_create_request.url)
    domain = Domain.create(
        created_at=datetime.datetime.now(),
        domain=".".join([extracted.subdomain, extracted.domain, extracted.suffix])
    )
    path = Path.create(
        created_at=datetime.datetime.now(),
        path=event_create_request.url,
        domain=domain
    )
    Event.create(
        created_at=datetime.datetime.now(),
        duration=event_create_request.duration,
        path=path
    )
