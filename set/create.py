import requests

# Constants
ACCESS_TOKEN = 'EAAQFcXItNR8BO2WYnFkztmmf1HxrnHwAXPANDs4ZA8RHc0teE1VQJXwNvDCh5CzzrmGe8oJofvZCkZBxMcIR3YvyazgSb8IBMTNVSpfiUOZC4nCZC1zQz7tM9HWFcVOXwAPEyT4H7aBXqN0vPjGBZBPWrjXYZCv6JZAxDf7MP3Twvi3ER6JDba2Pgse03Epl8YiRUhQhvJws9Wz7TFX7953TVksZBPAZDZD'
CATALOG_ID = '1518838045445568'
GRAPH_API_URL = f'https://graph.facebook.com/v17.0/{CATALOG_ID}/product_sets'

def create_product_set(name, filter_rule):
    """
    Creates a product set in the specified catalog.

    :param name: Name of the product set
    :param filter_rule: Rule to filter products for the set (e.g., '{"brand":{"eq":"Brand A"}}')
    """
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }
    data = {
        "name": name,
        "filter": filter_rule  # JSON filter rule
    }

    response = requests.post(GRAPH_API_URL, headers=headers, data=data)

    if response.status_code == 200:
        print("Product set created successfully:")
        print(response.json())
    else:
        print("Error creating product set:")
        print(f"Status Code: {response.status_code}")
        print(response.json())

# Example Usage
create_product_set("Brand A Products", '{"brand":{"eq":"Brand A"}}')