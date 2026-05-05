import requests
response = requests.get("https://restcountries.com/v3.1/name/canada")
data = response.json()[0]
print(f"Country: {data['name']['common']:>10}")
print(f"Capital: {data['capital'][0]:>10}")
print(f"Population: {data['population']:>5}")
print(f"Region: {data['region']:>13}")
print(f"Currency: {data['currencies']['CAD']['name']:>13}")