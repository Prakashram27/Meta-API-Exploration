import requests
import json

class MetaBusinessCatalogAPI:
    def __init__(self, access_token, business_id):
        """
        Initialize the Meta Business Catalog API client
        
        :param access_token: Facebook Graph API access token
        :param business_id: Business Account ID
        """
        self.base_url = "https://graph.facebook.com/v21.0"
        self.access_token = access_token
        self.business_id = business_id
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.access_token}'
        }

    def create_catalog(self, name, vertical='commerce'):
        """
        Create a new product catalog
        
        :param name: Name of the catalog
        :param vertical: Catalog vertical (default: commerce)
        :return: Created catalog ID
        """
        endpoint = f"{self.base_url}/{self.business_id}/product_catalogs"
        payload = {
            'name': name,
            'vertical': vertical,
            'access_token': self.access_token
        }
        
        try:
            response = requests.post(endpoint, json=payload, headers=self.headers)
            response.raise_for_status()
            return response.json().get('id')
        except requests.exceptions.RequestException as e:
            print(f"Error creating catalog: {e}")
            return None

    def delete_catalog(self, catalog_id):
        """
        Delete a product catalog
        
        :param catalog_id: ID of the catalog to delete
        :return: Boolean indicating success
        """
        endpoint = f"{self.base_url}/{catalog_id}"
        params = {'access_token': self.access_token}
        
        try:
            response = requests.delete(endpoint, params=params)
            response.raise_for_status()
            return True
        except requests.exceptions.RequestException as e:
            print(f"Error deleting catalog: {e}")
            return False

    def update_catalog(self, catalog_id, name=None, vertical=None):
        """
        Update an existing product catalog
        
        :param catalog_id: ID of the catalog to update
        :param name: New name for the catalog (optional)
        :param vertical: New vertical for the catalog (optional)
        :return: Boolean indicating success
        """
        endpoint = f"{self.base_url}/{catalog_id}"
        payload = {'access_token': self.access_token}
        
        if name:
            payload['name'] = name
        if vertical:
            payload['vertical'] = vertical
        
        try:
            response = requests.post(endpoint, json=payload, headers=self.headers)
            response.raise_for_status()
            return True
        except requests.exceptions.RequestException as e:
            print(f"Error updating catalog: {e}")
            return False

    def batch_catalog_operations(self, operations):
        """
        Perform batch operations on catalogs
        
        :param operations: List of batch operation dictionaries
        :return: Batch operation results
        """
        endpoint = f"{self.base_url}"
        payload = {
            'access_token': self.access_token,
            'batch': operations
        }
        
        try:
            response = requests.post(endpoint, json=payload, headers=self.headers)
            print(response.json)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error in batch operations: {e}")
            return None

    def list_catalogs(self,additional_fields=None):
        """
        List all product catalogs for the business account
        
        :return: List of catalogs
        """
        
        fields = ['id', 'name', 'vertical']
        if additional_fields:
            fields.extend(additional_fields)
        endpoint = f"{self.base_url}/{self.business_id}/product_catalogs"
        params = {
            'access_token': self.access_token,
            'fields': 'id,name,vertical'
        }
        
        try:
            response = requests.get(endpoint, params=params)
            response.raise_for_status()
            return response.json().get('data', [])
        except requests.exceptions.RequestException as e:
            print(f"Error listing catalogs: {e}")
            return []

# Example Usage
def main():
    # Replace with your actual access token and business ID
    ACCESS_TOKEN = ''
    BUSINESS_ID = ''
    
    # Initialize the API client
    catalog_api = MetaBusinessCatalogAPI(ACCESS_TOKEN, BUSINESS_ID)
    
    # Create a new catalog
    # new_catalog_id = catalog_api.create_catalog('My Product Catalog')
    # new_catalog_id = "1518838045445568"   
    operations = [
        {
        "name":'My New Product Catalog', 
        "vertical":'commerce',
        "additional_options":{
            'additional_vertical_option': 'LOCAL_PRODUCTS'
        }
    }
    ]

    
    
    catalog_api.batch_catalog_operations(operations=operations)
    
    # if new_catalog_id:
    #     # Update the catalog
    #     catalog_api.update_catalog(new_catalog_id, name='Updated Catalog Name')
        
    #     # Perform batch operations
    #     batch_ops = [
    #         {
    #             'method': 'POST',
    #             'relative_url': f'{new_catalog_id}',
    #             'body': json.dumps({'name': 'Batch Updated Catalog'})
    #         }
    #     ]
    #     batch_results = catalog_api.batch_catalog_operations(batch_ops)
        
        # List all catalogs
    # catalogs = catalog_api.list_catalogs()
    # catalogs = catalog_api.list_catalogs(additional_fields=['created_time'])
    # print("Existing Catalogs:", catalogs)
        
        # Optional: Delete the catalog
        # catalog_api.delete_catalog(new_catalog_id)

if __name__ == '__main__':
    main()
