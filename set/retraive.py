import requests
ACCESS_TOKEN = ''
CATALOG_ID = ''
GRAPH_API_URL = f'https://graph.facebook.com/v17.0/{CATALOG_ID}/product_sets'

def get_product_sets():
    """
    Retrieves all product sets for the specified catalog.
    """
    url = f"https://graph.facebook.com/v17.0/{CATALOG_ID}/product_sets"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print("Product sets retrieved successfully:")
        print(response.json())
    else:
        print("Error fetching product sets:")
        print(f"Status Code: {response.status_code}")
        print(response.json())

# Example Usage
get_product_sets()
