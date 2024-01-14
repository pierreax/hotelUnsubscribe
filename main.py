import requests

# Define the URL for the Sheety API
url = "https://api.sheety.co/f3a65c5d3619ab6b57dcfe118df98456/flightDeals/prices"

# Send a GET request to retrieve data
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    for row in data['prices']:
        # Assuming 'prices' is the key for your rows, you may need to adjust it if your data structure is different
        print("Row ID:", row['id'])
        # Add more fields as needed
        print()
else:
    print("Failed to fetch data. Status code:", response.status_code)
