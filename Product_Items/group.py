import requests

# Define the endpoint and access token
base_url = "https://graph.facebook.com/v21.0"  # Replace with the actual base URL
product_group_id = "8924809700912011"  # Replace with your product group ID
url = f"{base_url}/{product_group_id}/products"

# Prepare the payload
payload = {
    "name": "Stylish T-Shirt",
    "category": "Apparel",
    "price": 1999,  # Representing $19.99
    "image_url": "https://example.com/image.jpg",
    "retailer_id": "TSHIRT001",
    "availability": "in stock",
    "description": "A comfortable and stylish t-shirt, perfect for any occasion.",
    "brand": "Fashion Brand",
    "color": "Blue",
    "size": "M",
    "currency": "USD",
    "condition": "new",
    # Additional optional fields
    "additional_image_urls": ["https://example.com/image2.jpg"],
    "material": "Cotton",
    "sale_price": 1499,  # Representing $14.99
    "sale_price_start_date": "2024-12-01T00:00:00Z",
    "sale_price_end_date": "2024-12-10T23:59:59Z",
}

# Define headers
headers = {
    "Authorization": "Bearer EAAQFcXItNR8BO33gIeRmzE0wleFpWAhKDb6fPZAml5DruJ7pCY2NEa6xrvy3pxVFYLVZA6y7WxOIpjdO3CM02JOJOeMZA9FMlPd1zod73pF4ydY3myd8VqsIGdZAfCufV9p3XyQdoHbaKPhhafAud7bHEPxyZCm0hdX1IaQS7H9xvgdN26gC4VglFsZAxuBdfLZCIEWrnZCpGGitrEqmWK2M4FuCEQZDZD",  # Replace with your actual access token
    "Content-Type": "application/json",
}

# Make the POST request
response = requests.post(url, json=payload, headers=headers)

# Handle the response
if response.status_code == 200:
    print("Product created successfully:", response.json())
else:
    print("Failed to create product:", response.status_code, response.json())
