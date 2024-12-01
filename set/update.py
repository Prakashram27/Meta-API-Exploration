import requests

# Constants
ACCESS_TOKEN = ''
CATALOG_ID = ''
GRAPH_API_BASE_URL = f'https://graph.facebook.com/v21.0'


def update_product_set(product_set_id, update_data):
    """
    Updates a Product Set's attributes in the catalog.

    :param product_set_id: The ID of the product set to update.
    :param update_data: Dictionary containing the fields to update.
    """
    url = f"{GRAPH_API_BASE_URL}/{product_set_id}"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }

    response = requests.post(url, headers=headers, data=update_data)

    if response.status_code == 200:
        print(f"Product set {product_set_id} updated successfully!")
        print(response.json())
    else:
        print("Error updating product set:")
        print(f"Status Code: {response.status_code}")
        print(response.json())

# Example Usage
update_data = {
    "name": "Updated Product Set Name",  # Update the name
    "filter": '{"brand":{"eq":"Updated Brand"}}'  # Update the filter rule
}
update_product_set("881444887525851", update_data)
