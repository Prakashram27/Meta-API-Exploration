# import requests
# import json
# from typing import List, Dict, Optional, Union

# class FacebookCatalogAPI:
#     def __init__(self, access_token: str, api_version: str, business_id: str):
#         """
#         Initialize the Facebook Catalog API client.
        
#         Args:
#             access_token (str): Facebook API access token
#             api_version (str): API version (e.g., 'v16.0')
#             business_id (str): Facebook Business ID
#         """
#         self.access_token = access_token
#         self.api_version = api_version
#         self.business_id = business_id
#         self.base_url = f"https://graph.facebook.com/{api_version}"
        
#     def create_product_catalog(self, name: str) -> Dict:
#         """
#         Create a new product catalog.
        
#         Args:
#             name (str): Name of the catalog
            
#         Returns:
#             Dict: Response from the API
#         """
#         url = f"{self.base_url}/{self.business_id}/product_catalogs"
        
#         data = {
#             'name': name,
#             'access_token': self.access_token
#         }
        
#         response = requests.post(url, data=data)
#         response.raise_for_status()
#         return response.json()
    
#     def batch_update_items(
#         self,
#         catalog_id: str,
#         requests_data: List[Dict],
#         allow_upsert: bool = True,
#         item_sub_type: Optional[str] = None,
#         item_type: Optional[str] = None
#     ) -> Dict:
#         """
#         Batch update items in a product catalog.
        
#         Args:
#             catalog_id (str): ID of the product catalog
#             requests_data (List[Dict]): List of batch request objects
#             allow_upsert (bool, optional): Whether to allow upsert operations. Defaults to True.
#             item_sub_type (str, optional): Sub vertical type of items
#             item_type (str, optional): Type of items
            
#         Returns:
#             Dict: Response from the API
#         """
#         url = f"{self.base_url}/{catalog_id}/items_batch"
        
#         data = {
#             'access_token': self.access_token,
#             'allow_upsert': allow_upsert,
#             'requests': json.dumps(requests_data)
#         }
        
#         if item_sub_type:
#             data['item_sub_type'] = item_sub_type
            
#         if item_type:
#             data['item_type'] = item_type
            
#         response = requests.post(url, data=data)
#         response.raise_for_status()
#         return response.json()

# # Example usage
# if __name__ == "__main__":
#     # Initialize the API client
#     api = FacebookCatalogAPI(
#         access_token="EAAQFcXItNR8BOZCCUKkxQIESMcZCAuEj1KTTXkZAlKUcwkB1tN9RExTDrvZB8oY1396zpG0JzymgcnuZCuuM7z9ASJaHxeMSRZAbFdYcRajktvi0XUPRZCX5LopL3eD2dP2fWSehGTIN0XmjUgBGAUpoB8f7gjy79hmXdjGDsi5qP6mCG00m3t48dtxaAQXjckbfSSEjIzUVF7ZAMMbvZCscPYPSxLQZDZD",
#         api_version="v18.0",
#         business_id="1138893514424567"
#     )
    
#     # Create a new catalog
#     catalog_response = api.create_product_catalog(name="My Product Catalog")
#     catalog_id = catalog_response['id']
    
#     # Example batch update requests
#     batch_requests = [
#         {
#             "method": "CREATE",
#             "data": {
#                 "name": "Sample Product",
#                 "description": "Product description",
#                 "price": 99.99,
#                 "currency": "USD"
#             }
#         }
#     ]
    
#     # Perform batch update
#     batch_response = api.batch_update_items(
#         catalog_id=catalog_id,
#         requests_data=batch_requests,
#         item_type="product",
#         item_sub_type="ELECTRONICS_ACCESSORIES"
#     )


import requests
import json
from typing import List, Dict, Optional, Union

class FacebookCatalogAPI:
    def __init__(self, access_token: str, api_version: str="v18.0", business_id: str=None):
        """
        Initialize the Facebook Catalog API client.
        
        Args:
            access_token (str): Facebook API access token
            api_version (str): API version (e.g., 'v18.0')
            business_id (str): Facebook Business ID
        """
        self.access_token = access_token
        self.api_version = api_version
        self.business_id = business_id
        self.base_url = f"https://graph.facebook.com/{api_version}"
        
    def create_product_catalog(self, name: str) -> Dict:
        """
        Create a new product catalog.
        
        Args:
            name (str): Name of the catalog
            
        Returns:
            Dict: Response from the API
        """
        if not self.business_id:
            raise ValueError("Business ID is required")
            
        url = f"{self.base_url}/{self.business_id}/product_catalogs"
        
        data = {
            'name': name,
            'access_token': self.access_token
        }
        
        try:
            response = requests.post(url, data=data)
            response_json = response.json()
            
            if 'error' in response_json:
                print(f"Error: {response_json['error']['message']}")
                return response_json
                
            response.raise_for_status()
            return response_json
            
        except requests.exceptions.RequestException as e:
            print(f"API Request failed: {str(e)}")
            try:
                error_detail = response.json()
                print(f"Error details: {json.dumps(error_detail, indent=2)}")
            except:
                print(f"Status code: {response.status_code}")
            return None
    
    def batch_update_items(
        self,
        catalog_id: str,
        requests_data: List[Dict],
        allow_upsert: bool = True,
        item_sub_type: Optional[str] = None,
        item_type: Optional[str] = None
    ) -> Dict:
        """
        Batch update items in a product catalog.
        
        Args:
            catalog_id (str): ID of the product catalog
            requests_data (List[Dict]): List of batch request objects
            allow_upsert (bool, optional): Whether to allow upsert operations. Defaults to True.
            item_sub_type (str, optional): Sub vertical type of items
            item_type (str, optional): Type of items
            
        Returns:
            Dict: Response from the API
        """
        url = f"{self.base_url}/{catalog_id}/items_batch"
        
        data = {
            'access_token': self.access_token,
            'allow_upsert': allow_upsert,
            'requests': json.dumps(requests_data)
        }
        
        if item_sub_type:
            data['item_sub_type'] = item_sub_type
            
        if item_type:
            data['item_type'] = item_type
            
        try:
            response = requests.post(url, data=data)
            response_json = response.json()
            
            if 'error' in response_json:
                print(f"Error: {response_json['error']['message']}")
                return response_json
                
            response.raise_for_status()
            return response_json
            
        except requests.exceptions.RequestException as e:
            print(f"API Request failed: {str(e)}")
            try:
                error_detail = response.json()
                print(f"Error details: {json.dumps(error_detail, indent=2)}")
            except:
                print(f"Status code: {response.status_code}")
            return None

# Example usage with error handling
if __name__ == "__main__":
    # Your credentials
    ACCESS_TOKEN = "EAAQFcXItNR8BOZCCUKkxQIESMcZCAuEj1KTTXkZAlKUcwkB1tN9RExTDrvZB8oY1396zpG0JzymgcnuZCuuM7z9ASJaHxeMSRZAbFdYcRajktvi0XUPRZCX5LopL3eD2dP2fWSehGTIN0XmjUgBGAUpoB8f7gjy79hmXdjGDsi5qP6mCG00m3t48dtxaAQXjckbfSSEjIzUVF7ZAMMbvZCscPYPSxLQZDZD"  # Replace with your actual access token
    BUSINESS_ID = "1138893514424567"    # Replace with your actual business ID
    
    try:
        # Initialize the API client
        api = FacebookCatalogAPI(
            access_token=ACCESS_TOKEN,
            business_id=BUSINESS_ID
        )
        
        # Create a new catalog
        print("Creating product catalog...")
        catalog_response = api.create_product_catalog(name="My Product Catalog")
        
        if catalog_response and 'id' in catalog_response:
            catalog_id = catalog_response['id']
            print(f"Catalog created successfully with ID: {catalog_id}")
            
            # Example batch update requests
            batch_requests = [
                {
                    "method": "CREATE",
                    "data": {
                        "name": "Sample Product",
                        "description": "Product description",
                        "price": 99.99,
                        "currency": "USD"
                    }
                }
            ]
            
            # Perform batch update
            print("Performing batch update...")
            batch_response = api.batch_update_items(
                catalog_id=catalog_id,
                requests_data=batch_requests,
                item_type="product",
                item_sub_type="ELECTRONICS_ACCESSORIES"
            )
            
            if batch_response:
                print("Batch update completed successfully")
                print(json.dumps(batch_response, indent=2))
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")