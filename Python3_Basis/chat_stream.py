import aiohttp
import asyncio

if __name__ == '__main__':
    async def fetch_sse(url, payload):
        headers = {
            "Content-Type": "application/json",
            "Accept": "text/event-stream",
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload, headers=headers) as response:
                if response.status == 200:
                    print("Connected successfully, streaming data...\n")
                    async for line in response.content:
                        decoded_line = line.decode('utf-8').strip()
                        data = decoded_line[len("data: ") - 1:]
                        print("Received data:", data)
                else:
                    print(f"Failed to connect. Status code: {response.status}")

    # URL and payload setup
    url = "url"
    payload = {
        "question": "How do I confess my sins to God?",
        "userId": 607735609,
        "appFlag": 262144,
        "chatType": 0,
        "days": 1,
        "initialQuestionId": 4
    }

    # Run the event loop
    asyncio.run(fetch_sse(url, payload))
