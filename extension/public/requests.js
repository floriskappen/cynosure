
const API_ENDPOINT = 'http://localhost:8000'

async function createEvent(url, action) {
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
