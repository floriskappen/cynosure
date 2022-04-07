
import datetime
from tldextract import tldextract

from fastapi import APIRouter
from pydantic import BaseModel

from entities.events.model import Event
from entities.sessions.model import Session
from entities.event_chains.functions import get_or_create_event_chain, create_event_chain
from entities.domains.model import Domain

router = APIRouter()

class EventCreateRequest(BaseModel):
    url: str
    action: int

@router.post("")
async def create(event_create_request: EventCreateRequest):

    # Create or get the domain
    extracted_url = tldextract.extract(event_create_request.url)
    domain = Domain.get_or_create(
        domain=".".join([extracted_url.subdomain, extracted_url.domain, extracted_url.suffix]),
        defaults={
            "created_at": datetime.datetime.now()
        }
    )[0]

    # If it's a create action then we need to make a new event chain
    if event_create_request.action == 1:
        event_chain = create_event_chain(domain)
    # Create or get the active event chain related to this domain
    else:
        event_chain = get_or_create_event_chain(domain)
    Event.create(
        created_at=datetime.datetime.now(),
        path=event_create_request.url,
        event_chain=event_chain,
        action=event_create_request.action
    )
