import requests
import pandas as pd

def request_api(produto):
    url = f"https://api.mercadolibre.com/sites/MLB/search?q={produto}"
    response = requests.get(url)
    return response.json()

data = request_api("cofre")


def extrair_dados(json_data):
    results = json_data.get('results', [])
    extracted_data = []
    for item in results:
        extracted_data.append({
            'title': item.get('title', ''),
            'seller': item.get('seller', {}).get('id', ''),
            'category_id': item.get('category_id', {}),
            'price': item.get('price', 0),
            'available_quantity': item.get('available_quantity', 0),
            'original_price': item.get('original_price') if item.get('original_price') is not None else item.get('price', 0)
        })
    return extracted_data


products = extrair_dados(data)

# print(products)

df = pd.DataFrame(products)
df.to_csv('dados_meli.csv', index=False)
