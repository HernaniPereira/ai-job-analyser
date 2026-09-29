import httpx


async def fetch_data(url):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, timeout=5.0)
            response.raise_for_status()

    except httpx.HTTPStatusError as error:
        print("Failed to fetch data", error.response.status_code)
        return

    except httpx.RequestError as error:
        print("Could not connect to the server", error)
        return
    return response.json()
