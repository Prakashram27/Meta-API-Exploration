import json
import requests
import random

# # Constants
# ACCESS_TOKEN = ''
# CATALOG_ID = 'your_catalog_id'
# DUMMY_PRODUCTS_FILE = "dummy_products.json"

ACCESS_TOKEN = 'EAAQFcXItNR8BO23Ky7141NqODYAi9mfqnbjlq6usfFczX3AMKJL31sQaXZC22eETlnYIBljmDfyPf9lXgWCV1R2aJM6ZA8wxzIa9kx97pvrvvJRlZCtABRzlNeZAyZCwwczH2AS1gTyi8ZCgMaZAwuYxZBABJgj2yV168hSPrhvxKulQkCNNYZBJOAT686O4nUgfpXDzUr2feZCZCPImwHLNOPsOIeZC5wZDZD'
# APP_ID = '1131884711851295'
APP_SECRET = '1fef7713aa9e1758887277a4ba6beef7'
CATALOG_ID = '1518838045445568' 
GRAPH_API_URL = f'https://graph.facebook.com/v21.0/{CATALOG_ID}/batch'
DUMMY_PRODUCTS_FILE = "dummy_products.json"


# Function to generate dummy product data
def generate_dummy_products():
    products = []
    for i in range(1, 2001):  # Generate 300 products
        currency = random.choice(["USD", "INR"])
        price = random.randint(10, 500)  # Random price between 10 and 500
        product = {
            "retailer_id": f"product_{i:03d}",
            "method": "CREATE",
            "data": {
                "name": f"Product {i}",
                "description": f"Description for Product {i}",
                "availability": "in stock",
                "condition": "new",
                "price": price,
                "currency": currency,
                "brand": f"Brand {random.choice(['A', 'B', 'C', 'D'])}",
                "image_url": f"https://example.com/product{i}.jpg",
                "url": f"https://example.com/product{i}",
                "visibility": "published"
            }
        }
        products.append(product)
    return products

# Save dummy products to JSON file
def save_products_to_file(products, file_path):
    with open(file_path, "w") as f:
        json.dump(products, f, indent=4)
    print(f"Saved {len(products)} products to {file_path}")

# Load products from file
def load_products_from_file(file_path):
    with open(file_path, "r") as f:
        return json.load(f)

# Upload products using Facebook Batch API
def upload_products_to_facebook(products):
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }
    payload = {
        "allow_upsert": True,
        "requests": products
    }
    response = requests.post(GRAPH_API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        print("Batch upload successful!")
        print(response.json())
    else:
        print("Error during batch upload:")
        print(f"Status Code: {response.status_code}")
        print(response.json())

# Main logic
if __name__ == "__main__":
    # Generate and save dummy products
    dummy_products = generate_dummy_products()
    save_products_to_file(dummy_products, DUMMY_PRODUCTS_FILE)
    
    # Load dummy products from the file
    products_to_upload = load_products_from_file(DUMMY_PRODUCTS_FILE)
    
    # Upload products to Facebook Batch API
    upload_products_to_facebook(products_to_upload)
