import requests

def fetch_data(produto):
    url = f"https://api.mercadolibre.com/sites/MLB/search?q={produto}"
    response = requests.get(url)
    return response.json()

data = fetch_data("cofre")


def list_keys(json_data):
    results = json_data.get('results', [])
    if results:
        first_item = results[0]
        return first_item.keys()
    else:
        return []

keys = list_keys(data)
# print(keys)


def extract_data(json_data):
    results = json_data.get('results', [])
    extracted_data = []
    for item in results:
        extracted_data.append({
            'title': item.get('title', ''),
            'seller': item.get('seller', ''),
            'price': item.get('price', 0),
            'available_quantity': item.get('available_quantity', 0),
            'original_price': item.get('original_price', 0)
        })
    return extracted_data

products = extract_data(data)

print(products)