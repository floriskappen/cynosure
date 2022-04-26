
const API_ENDPOINT = 'http://localhost:8000'

async function eventRequest(url, action) {
    const response = await fetch(
        `${API_ENDPOINT}/events`,
        {
            method: 'POST',
            headers: {
                'Content-Type': 'applications/json'
            },
            body: JSON.stringify({
                url,
                action
            })
        }
    )
    return response.json()
}

async function pingRequest(eventChainId) {
    const response = await fetch(
        `${API_ENDPOINT}/event_chains/ping` + new URLSearchParams({
            event_chain_id: eventChainId
        }),
        {
            method: 'POST',
        }
    )
    return response.json()
}
