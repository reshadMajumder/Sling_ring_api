import asyncio
import threading
import time
import httpx
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse

# Global variable to store fetched exoplanet data
exoplanet_data = {"data": [], "status": "Fetching data..."}

# Async function to fetch data
async def fetch_data():
    url = "https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=cumulative&format=json"
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()
            return response.json()
    except Exception as e:
        return {"status": f"Error: {str(e)}"}

# Function to run the async fetch_data function in a separate event loop
def start_fetching():
    global exoplanet_data

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    while True:
        fetched_data = loop.run_until_complete(fetch_data())
        if "status" not in fetched_data:
            exoplanet_data["data"] = fetched_data
            exoplanet_data["status"] = "Data fetched successfully"
            print("Data updated successfully in the background.")
        else:
            exoplanet_data["status"] = fetched_data["status"]
            print(f"Error while fetching data: {exoplanet_data['status']}")
        
        # Fetch data every 10 seconds (adjust as needed)
        time.sleep(10)

# Start the background thread to fetch data continuously
thread = threading.Thread(target=start_fetching)
thread.daemon = True  # Daemonize the thread to run in the background
thread.start()

@api_view(['GET'])
def get_exoplanet_data(request):
    # Return the most recent fetched data
    return Response(exoplanet_data["data"], status=status.HTTP_200_OK)
