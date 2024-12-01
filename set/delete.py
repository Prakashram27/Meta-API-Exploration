
import requests
ACCESS_TOKEN = 'EAAQFcXItNR8BO2WYnFkztmmf1HxrnHwAXPANDs4ZA8RHc0teE1VQJXwNvDCh5CzzrmGe8oJofvZCkZBxMcIR3YvyazgSb8IBMTNVSpfiUOZC4nCZC1zQz7tM9HWFcVOXwAPEyT4H7aBXqN0vPjGBZBPWrjXYZCv6JZAxDf7MP3Twvi3ER6JDba2Pgse03Epl8YiRUhQhvJws9Wz7TFX7953TVksZBPAZDZD'
CATALOG_ID = '1518838045445568'
GRAPH_API_URL = f'https://graph.facebook.com/v21.0'


def delete_product_set(product_set_id):
    """
    Deletes a product set by ID.

    :param product_set_id: ID of the product set to delete
    """
    url = f"https://graph.facebook.com/v17.0/{product_set_id}"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }

    response = requests.delete(url, headers=headers)

    if response.status_code == 200:
        print(f"Product set {product_set_id} deleted successfully!")
    else:
        print("Error deleting product set:")
        print(f"Status Code: {response.status_code}")
        print(response.json())

# Example Usage
delete_product_set("881444887525851")
