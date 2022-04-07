
from typing import List
import datetime
import pytz


from entities.event_chains.model import EventChain
from entities.domains.model import Domain
from entities.sessions.functions import get_or_create_session

def get_or_create_event_chain(domain: Domain):

    # Get the most recent event chain
    current_event_chains: List[EventChain] = EventChain.select().order_by(-EventChain.created_at)
    if current_event_chains.count() > 0:
        current_event_chain = current_event_chains[0]
        # Check if the domain matches and if it's still active
        if current_event_chain.domain == domain and not current_event_chain.is_closed:
            return current_event_chain

    return create_event_chain(domain)

def create_event_chain(domain: Domain):
    return EventChain.create(
        created_at=datetime.datetime.now(pytz.timezone("Europe/Amsterdam")),
        domain=domain,
        session=get_or_create_session(),
        last_ping=datetime.datetime.now(pytz.timezone("Europe/Amsterdam")),
    )
