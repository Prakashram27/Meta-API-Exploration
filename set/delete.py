
import requests
ACCESS_TOKEN = ''
CATALOG_ID = ''
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
