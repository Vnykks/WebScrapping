# Import required libraries
import pandas as pd
import requests

# API key
api_key = "1806f934-807e-4a24-b6b5-be3e958dd947"
url_template = "https://content.guardianapis.com/world/narendra-modi?from-date=2021-01-01&api-key={}&type=article&page=".format(api_key)

# Create a list of URLs for multiple pages
urllist = [url_template + str(i) for i in range(1, 10)]

# Initialize a list to store the JSON responses
info = []

# Function to fetch JSON from a URL
def fetch_json(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        info.append(data)
    else:
        print(f"Failed to fetch data for URL {url}, Status code: {response.status_code}")

# Fetch data from each URL and store in 'info'
for url in urllist:
    fetch_json(url)

# Example of extracting specific data from JSON response
if len(info) >= 10:
    title = info[9]['response']['results'][9]['webTitle']
    print("Sample Title:", title)

# Convert 'info' into a DataFrame
finallist = [item for data in info for item in data['response']['results']]
datanew = pd.DataFrame(finallist)

# Display the DataFrame and JSON data list
print(datanew)
print(info)


