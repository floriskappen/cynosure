
from typing import List
import pytz
import datetime

from entities.sessions.model import Session
from entities.event_chains.model import EventChain

def get_or_create_session():
    # Get the most recent session
    session_query: List[Session] = Session.select().order_by(-Session.created_at)
    if session_query.count() > 0:
        recent_session = session_query[0]
        
        # Get the most recent event chain in this session
        event_chain_query = EventChain.select().where(EventChain.session == recent_session.id).order_by(-EventChain.last_ping)
        if event_chain_query.count() > 0:
            event_chain = event_chain_query[0]
            
            # If the last activity was less than 30min ago we return the session
            latest_event_datetime = event_chain.last_ping
            now = datetime.datetime.now(pytz.timezone("Europe/Amsterdam"))
            minutes_difference = (now - latest_event_datetime).total_seconds() / 60.0
            if minutes_difference < 30:
                return recent_session
    
    return Session.create(
        created_at=datetime.datetime.now(pytz.timezone("Europe/Amsterdam"))
    )
