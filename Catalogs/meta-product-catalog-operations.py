import requests
import json
import logging

class MetaProductCatalogAPI:
    def __init__(self, access_token, business_id):
        """
        Initialize Meta Product Catalog API client
        
        :param access_token: Facebook Graph API access token
        :param business_id: Business Account ID
        """
        self.base_url = "https://graph.facebook.com/v19.0"
        self.access_token = access_token
        self.business_id = business_id
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.access_token}'
        }
        
        # Configure logging
        logging.basicConfig(level=logging.INFO, 
                            format='%(asctime)s - %(levelname)s: %(message)s')
        self.logger = logging.getLogger(__name__)

    def create_catalog(self, name, vertical='commerce', additional_options=None):
        """
        Create a new product catalog
        
        :param name: Name of the catalog
        :param vertical: Catalog vertical (default: commerce)
        :param additional_options: Optional additional catalog settings
        :return: Created catalog ID or None
        """
        endpoint = f"{self.base_url}/{self.business_id}/owned_product_catalogs"
        
        payload = {
            'name': name,
            'vertical': vertical,
            'access_token': self.access_token
        }
        
        # Add additional options if provided
        if additional_options:
            payload.update(additional_options)
        
        try:
            response = requests.post(endpoint, json=payload, headers=self.headers)
            response.raise_for_status()
            catalog_id = response.json().get('id')
            self.logger.info(f"Catalog created successfully. ID: {catalog_id}")
            return catalog_id
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Error creating catalog: {e}")
            self.logger.error(f"Response: {response.text}")
            return None

    def update_catalog(self, catalog_id, name=None, additional_settings=None):
        """
        Update an existing product catalog
        
        :param catalog_id: ID of the catalog to update
        :param name: New name for the catalog
        :param additional_settings: Additional catalog settings to update
        :return: Boolean indicating success
        """
        endpoint = f"{self.base_url}/{catalog_id}"
        
        payload = {
            'access_token': self.access_token
        }
        
        if name:
            payload['name'] = name
        
        if additional_settings:
            payload.update(additional_settings)
        
        try:
            response = requests.post(endpoint, json=payload, headers=self.headers)
            response.raise_for_status()
            self.logger.info(f"Catalog {catalog_id} updated successfully")
            return True
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Error updating catalog: {e}")
            self.logger.error(f"Response: {response.text}")
            return False

    def delete_catalog(self, catalog_id, force_delete=False):
        """
        Delete a product catalog
        
        :param catalog_id: ID of the catalog to delete
        :param force_delete: Force deletion even with live product sets
        :return: Boolean indicating success
        """
        endpoint = f"{self.base_url}/{catalog_id}"
        
        params = {
            'access_token': self.access_token,
            'allow_delete_catalog_with_live_product_set': force_delete
        }
        
        try:
            response = requests.delete(endpoint, params=params)
            response.raise_for_status()
            self.logger.info(f"Catalog {catalog_id} deleted successfully")
            return True
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Error deleting catalog: {e}")
            self.logger.error(f"Response: {response.text}")
            return False

    def list_catalogs(self, additional_fields=None):
        """
        List all product catalogs for the business account
        
        :param additional_fields: List of additional fields to retrieve
        :return: List of catalogs
        """
        endpoint = f"{self.base_url}/{self.business_id}/owned_product_catalogs"
        
        # Default fields
        fields = ['id', 'name', 'vertical', 'product_count']
        
        # Add additional fields if provided
        if additional_fields:
            fields.extend(additional_fields)
        
        params = {
            'access_token': self.access_token,
            'fields': ','.join(fields)
        }
        
        try:
            response = requests.get(endpoint, params=params)
            response.raise_for_status()
            catalogs = response.json().get('data', [])
            self.logger.info(f"Retrieved {len(catalogs)} catalogs")
            return catalogs
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Error listing catalogs: {e}")
            self.logger.error(f"Response: {response.text}")
            return []

    def manage_external_event_sources(self, catalog_id, pixel_ids=None, app_ids=None, action='add'):
        """
        Manage external event sources (pixels, apps) for a catalog
        
        :param catalog_id: ID of the catalog
        :param pixel_ids: List of pixel IDs to add/remove
        :param app_ids: List of app IDs to add/remove
        :param action: 'add' or 'remove'
        :return: Boolean indicating success
        """
        if action not in ['add', 'remove']:
            self.logger.error("Invalid action. Use 'add' or 'remove'.")
            return False
        
        endpoint = f"{self.base_url}/{catalog_id}/external_event_sources"
        
        # Prepare payload
        payload = {
            'access_token': self.access_token
        }
        
        if pixel_ids:
            payload['external_event_sources'] = pixel_ids
        
        if app_ids:
            payload['external_event_sources'] = app_ids
        
        try:
            if action == 'add':
                response = requests.post(endpoint, json=payload, headers=self.headers)
            else:
                response = requests.delete(endpoint, json=payload, headers=self.headers)
            
            response.raise_for_status()
            self.logger.info(f"External event sources {'added' if action == 'add' else 'removed'} successfully")
            return True
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Error {'adding' if action == 'add' else 'removing'} external event sources: {e}")
            self.logger.error(f"Response: {response.text}")
            return False

def main():
    # Replace with your actual credentials
    ACCESS_TOKEN = ''
    BUSINESS_ID = ''
    
    # Initialize the API client
    catalog_api = MetaProductCatalogAPI(ACCESS_TOKEN, BUSINESS_ID)
    
    catalog_id = ""
    
    catalog_api.manage_external_event_sources(catalog_id=catalog_id)
    
    
    # Example workflow
    # 1. List existing catalogs
    # existing_catalogs = catalog_api.list_catalogs()
    # for catalog in existing_catalogs:
    #     print(f"Catalog: {catalog['name']} (ID: {catalog['id']})")
    
    # 2. Create a new catalog
    # new_catalog_id = catalog_api.create_catalog(
    #     name='My New Product Catalog', 
    #     vertical='commerce',
    #     additional_options={
    #         'additional_vertical_option': 'LOCAL_PRODUCTS'
    #     }
    # )
    
    # if new_catalog_id:
    #     # 3. Update the catalog
    #     catalog_api.update_catalog(
    #         new_catalog_id, 
    #         name='Updated Product Catalog'
    #     )
        
    #     # 4. Manage external event sources (e.g., pixels)
    #     catalog_api.manage_external_event_sources(
    #         new_catalog_id, 
    #         pixel_ids=['PIXEL_ID_1', 'PIXEL_ID_2']
    #     )
        
        # 5. Optional: Delete the catalog (uncomment with caution)
        # catalog_api.delete_catalog(new_catalog_id, force_delete=True)

if __name__ == '__main__':
    main()
