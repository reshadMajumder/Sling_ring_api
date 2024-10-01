import threading
import time
import httpx
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from asgiref.sync import async_to_sync  


# Global variable to store fetched exoplanet data
exoplanet_data = {"data": [], "status": "Fetching data..."}

# Define a background thread to fetch data periodically
def background_fetch_data():
    global exoplanet_data

    url = "https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=cumulative&format=json"

    while True:
        try:
            async def fetch_data():
                async with httpx.AsyncClient() as client:
                    response = await client.get(url)
                    response.raise_for_status()
                    return response.json()

            # Using async_to_sync to run the async fetch_data function
            exoplanet_data["data"] = async_to_sync(fetch_data)()
            exoplanet_data["status"] = "Data fetched successfully"
            print("Data updated successfully in the background.")
        except Exception as e:
            exoplanet_data["status"] = f"Error: {str(e)}"
            print(f"Error while fetching data: {e}")
        
        # Fetch data every 10 seconds (adjust as needed)
        time.sleep(10)

# Start the background thread to fetch data continuously
thread = threading.Thread(target=background_fetch_data)
thread.daemon = True  # Daemonize the thread to run in the background
thread.start()

@api_view(['GET'])
def get_exoplanet_data(request):
    # Return the most recent fetched data
    return Response(exoplanet_data["data"], status=status.HTTP_200_OK)
