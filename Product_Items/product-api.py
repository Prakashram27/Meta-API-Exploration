import requests
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.productitem import ProductItem

# Initialize the Facebook API
ACCESS_TOKEN = 'EAAQFcXItNR8BO33gIeRmzE0wleFpWAhKDb6fPZAml5DruJ7pCY2NEa6xrvy3pxVFYLVZA6y7WxOIpjdO3CM02JOJOeMZA9FMlPd1zod73pF4ydY3myd8VqsIGdZAfCufV9p3XyQdoHbaKPhhafAud7bHEPxyZCm0hdX1IaQS7H9xvgdN26gC4VglFsZAxuBdfLZCIEWrnZCpGGitrEqmWK2M4FuCEQZDZD'
APP_ID = '1131884711851295'
APP_SECRET = '1fef7713aa9e1758887277a4ba6beef7'
CATALOG_ID = '1518838045445568'  
GRAPH_API_URL = f'https://graph.facebook.com/v21.0/{CATALOG_ID}/batch'
GRAPH_API_BASE_URL = "https://graph.facebook.com/v21.0"

FacebookAdsApi.init(access_token=ACCESS_TOKEN)

############################################## GET PRODUCT ITEM ######################################################
def get_product_item(product_item_id):
    try:
        product_item = ProductItem(product_item_id).api_get(fields=[
            'id', 
            'name',
        ])
        print("Product Item Details:")
        print(product_item)
    except Exception as e:
        print("Error retrieving product item:", e)

# Replace 'your_product_item_id' with the actual product ID
# product_item_id = '1518838045445568'
# get_product_item(product_item_id)


############################################## CREATE PRODUCT ITEM #####################################################
def create_product_item():
    try:
        product_obj = ProductItem(parent_id=CATALOG_ID)
        product = product_obj.api_create(
            fields={},
            params={
                'retailer_id': 'product_1233',  # Unique ID for the product in your system
                'name': 'tEST1',
                'description': 'This is a sample product description',
                'availability': 'in stock',  # Can be 'in stock', 'out of stock', or 'preorder'
                'condition': 'new',  # Can be 'new', 'used', or 'refurbished'
                'price': 19,  # Price in the format: 'amount currency'
                'currency':'USD',
                'brand': 'Sample Brand',
                'image_url': 'https://example.com/product-image.jpg',  # Image URL
                'url': 'https://example.com/product',  # Link to the product page
                'visibility': 'published',  # Can be 'published' or 'staging'
            },
            parent_id=CATALOG_ID
        )
        print("Product item created successfully:", product)
    except Exception as e:
        print("Error creating product item:", e)
        
# create_product_item()

#########################################BATCH PRODUCT ITEM CREATE####################################################
def create_batch_product():
    # Define the batch request payload
    batch_requests = [
        {
            "retailer_id": "product_001",  # Unique ID for the product
            "method": "CREATE",
            "data": {
                "name": "Product 1",
                "description": "Description for Product 1",
                "availability": "in stock",
                "condition": "new",
                "price": 19,
                "currency":"USD",
                "brand": "Brand A",
                "image_url": "https://example.com/product1.jpg",
                "url": "https://example.com/product1",
                "visibility": "published"
            }
        },
        {
            "retailer_id": "product_002",
            "method": "CREATE",
            "data": {
                "name": "Product 2",
                "description": "Description for Product 2",
                "availability": "in stock",
                "condition": "new",
                "price": 29,
                "currency":"USD",
                "brand": "Brand B",
                "image_url": "https://example.com/product2.jpg",
                "url": "https://example.com/product2",
                "visibility": "published"
            }
        }
    ]

    # API call headers and payload
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }
    payload = {
        "allow_upsert": True,  # Create items if they don't already exist
        "requests": batch_requests
    }

    # Make the POST request
    response = requests.post(GRAPH_API_URL, headers=headers, json=payload)

    # Process the response
    if response.status_code == 200:
        response_data = response.json()
        print("Batch upload successful!")
        print(response_data)
    else:
        print("Error during batch upload:")
        print(f"Status Code: {response.status_code}")
        print(response.json())
        
# create_batch_product()


############################################# UPDATE ###################################################
def update_product_item(product_item_id, updated_data):
    """
    Updates fields for a specific product item in the catalog.
    """
    url = f"{GRAPH_API_BASE_URL}/{product_item_id}"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }
    response = requests.post(url, headers=headers, data=updated_data)

    if response.status_code == 200:
        print(f"Product item {product_item_id} updated successfully!")
        print(response.json())
    else:
        print("Error during update:")
        print(f"Status Code: {response.status_code}")
        print(response.json())

# Example Usage
update_data = {
    "name": "Updated Product Name",
    "price": 1000,
    "availability": "in stock"
}
# update_product_item("8532629666865563", update_data)

    

    
    
############################################### DELETE ####################################################
# Constants
GRAPH_API_BASE_URL = 'https://graph.facebook.com/v17.0'

def delete_product_item(product_item_id):
    """
    Deletes a product item from the catalog.
    """
    url = f"{GRAPH_API_BASE_URL}/{product_item_id}"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }

    response = requests.delete(url, headers=headers)

    if response.status_code == 200:
        print(f"Product item {product_item_id} deleted successfully!")
    else:
        print("Error during deletion:")
        print(f"Status Code: {response.status_code}")
        print(response.json())

# Example Usage
# delete_product_item("8533034673490873")


# def get_catalog_products(access_token, catalog_id, fields=None):
#     """
#     Fetch product items from a Meta catalog using the Graph API
    
#     Parameters:
#     access_token (str): Your Meta Graph API access token
#     catalog_id (str): ID of your product catalog
#     fields (list): Optional list of fields to retrieve for each product
    
#     Returns:
#     dict: API response containing product items
#     """
#     base_url = f"https://graph.facebook.com/v18.0/{catalog_id}/products"
#     if fields is None:
#         fields = [
#             'id',
#             'name',
#             'description',
#             'price',
#             'currency',
#             'availability',
#             'condition',
#             'brand',
#             'image_url'
#         ]

#     params = {
#         'access_token': access_token,
#         'fields': ','.join(fields)
#     }
    
#     try:
#         response = requests.get(base_url, params=params)
#         response.raise_for_status()
#         return response.json()
        
#     except requests.exceptions.RequestException as e:
#         print(f"Error fetching products: {e}")
#         return None

# def main():
#     # Your credentials and catalog ID
#     ACCESS_TOKEN = 'EAAQFcXItNR8BOZCCUKkxQIESMcZCAuEj1KTTXkZAlKUcwkB1tN9RExTDrvZB8oY1396zpG0JzymgcnuZCuuM7z9ASJaHxeMSRZAbFdYcRajktvi0XUPRZCX5LopL3eD2dP2fWSehGTIN0XmjUgBGAUpoB8f7gjy79hmXdjGDsi5qP6mCG00m3t48dtxaAQXjckbfSSEjIzUVF7ZAMMbvZCscPYPSxLQZDZD'
#     CATALOG_ID = '1518838045445568'
    
#     # Optional: Specify custom fields
#     custom_fields = [
#     ]
    
#     # Get products
#     products = get_catalog_products(ACCESS_TOKEN, CATALOG_ID, custom_fields)
    
#     # Process results
#     if products and 'data' in products:
#         for product in products['data']:
#             print(f"Product ID: {product.get('id')}")
#             print(f"Name: {product.get('name')}")
#             print(f"Price: {product.get('price')}")
#             print("-------------------")
    
#     # Handle pagination if more products exist
#     next_page = products.get('paging', {}).get('next')
#     while next_page:
#         response = requests.get(next_page)
#         if response.status_code == 200:
#             products = response.json()
#             for product in products['data']:
#                 print(f"Product ID: {product.get('id')}")
#                 print(f"Name: {product.get('name')}")
#                 print(f"Price: {product.get('price')}")
#                 print("-------------------")
#             next_page = products.get('paging', {}).get('next')
#         else:
#             break

# if __name__ == "__main__":
#     main()

