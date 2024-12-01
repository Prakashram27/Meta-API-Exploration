# import requests

# def create_product_catalog(name: str, vertical: str = "commerce"):
#     """
#     Create a new product catalog for the ad account
    
#     Args:
#         name (str): Name of the catalog
#         vertical (str): Catalog vertical (e.g., 'commerce', 'vehicles', 'hotels')
        
#     Returns:
#         dict: Created catalog information
#     """
#     data = {
#         "name": name,
#         "vertical": vertical
#     }
#     access_token = 'EAAQFcXItNR8BOZCCUKkxQIESMcZCAuEj1KTTXkZAlKUcwkB1tN9RExTDrvZB8oY1396zpG0JzymgcnuZCuuM7z9ASJaHxeMSRZAbFdYcRajktvi0XUPRZCX5LopL3eD2dP2fWSehGTIN0XmjUgBGAUpoB8f7gjy79hmXdjGDsi5qP6mCG00m3t48dtxaAQXjckbfSSEjIzUVF7ZAMMbvZCscPYPSxLQZDZD'
#     # headers = {
#     #         "access_token": f"{access_token}",
#     #         "Content-Type": "application/json"
#     #     }
#     params = {
#         'access_token': access_token,
#     }
#     method = 'POST'
#     url = 'https://graph.facebook.com/22.0/1138893514424567/product_catalogs'
    
#     try:
#         response = requests.request(
#             method=method,
#             url=url,
#             params=params,
#             json=data,
#             # headers=headers
#         )
#         response.raise_for_status()
        
#         print(response.json)
#         return response.json()
#     except requests.exceptions.RequestException as e:
#         raise Exception(f"API request failed: {str(e)}")
    
    
# create_product_catalog(name="Catalog_Code_Test")


import requests
import json

def create_product_catalog(name: str, vertical: str = "commerce"):
    """
    Create a new product catalog for the ad account
    
    Args:
        name (str): Name of the catalog
        vertical (str): Catalog vertical (e.g., 'commerce', 'vehicles', 'hotels')
        
    Returns:
        dict: Created catalog information
    """
    # Your access token
    access_token = 'EAAQFcXItNR8BOZCCUKkxQIESMcZCAuEj1KTTXkZAlKUcwkB1tN9RExTDrvZB8oY1396zpG0JzymgcnuZCuuM7z9ASJaHxeMSRZAbFdYcRajktvi0XUPRZCX5LopL3eD2dP2fWSehGTIN0XmjUgBGAUpoB8f7gjy79hmXdjGDsi5qP6mCG00m3t48dtxaAQXjckbfSSEjIzUVF7ZAMMbvZCscPYPSxLQZDZD'
    
    # The ad account ID should include 'act_' prefix
    ad_account_id = '1138893514424567'
    
    # Correct API version and endpoint
    url = f'https://graph.facebook.com/v21.0/{ad_account_id}/product_catalogs'
    
    # Data payload
    data = {
        "name": name,
        "vertical": vertical,
    }
    
    params = {
        "access_token": access_token
    }
    
    data = {
    "name": "Catalog",
    
}
    
    # Headers are important
    # headers = {
    #     "Authorization": f"Bearer {access_token}",
    #     "Content-Type": "application/json"
    # }
    
    try:
        response = requests.post(
            url=url,
            params=params,
            # headers=headers,
            json=data
        )
        
        # Print response for debugging
        print("Status Code:", response.status_code)
        print("Response:", response.text)
        
        # Check if the request was successful
        response.raise_for_status()
        
        return response.json()
    
    except requests.exceptions.RequestException as e:
        print(f"API request failed: {str(e)}")
        return None

# Test the function
result = create_product_catalog(
    name="Catalog_Code_Test",
    vertical="commerce"
)

if result:
    print("Success:", json.dumps(result, indent=2))