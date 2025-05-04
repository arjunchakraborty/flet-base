from flet import *
import requests
import aiohttp
import asyncio

#Replace this url with one that requires credentials
TEST_URL = "http://127.0.0.1:8000/AUTH_REQUIRED"

def build_request(page, url, data=None, authenticated=True):
    """
    Helper function to build requests with optional authentication
    """
    headers = {}
    if authenticated:
        token = page.client_storage.get('access')
        headers['Authorization'] = f'Bearer {token}'
    
    if data:  # POST request
        rsp = requests.post(url=url, data=data, headers=headers)
    else:  # GET request
        rsp = requests.get(url=url, headers=headers)
    
    return rsp

async def async_build_request(page, url, data=None, authenticated=True):
    """
    Async helper function to build requests with optional authentication
    """
    headers = {}
    if authenticated:
        token = await page.client_storage.get_async('access')
        headers['Authorization'] = f'Bearer {token}'
    
    async with aiohttp.ClientSession() as session:
        try:
            if data:  # POST request
                async with session.post(url, data=data, headers=headers) as response:
                    response_data = await response.json()
            else:  # GET request
                async with session.get(url, headers=headers) as response:
                    response_data = await response.json()
            
            return {
                'status': response.status,
                'data': response_data,
                'headers': response.headers
            }
        except aiohttp.ClientError as e:
            print(f"Request error: {str(e)}")
            return {'status': 500, 'error': str(e)}
        except json.JSONDecodeError:
            print("Failed to decode JSON response")
            return {'status': 500, 'error': 'Invalid JSON response'}

def check_auth(page) -> bool:
    """Check if there is a logged in user and his credential
    are still valid"""
    try:
        if token := page.client_storage.get('access'):
            response = build_request(page, TEST_URL)
            if response.status_code == 200:
                print("Auth validated")
                return True
            print(f"Auth failed - Status: {response.status_code}")
            return False
        print("No auth token found")
        return False
    
    except Exception as e:
        print(f"Auth check error: {str(e)}")
        return False

async def async_check_auth(page) -> bool:
    """
    Async check if user is authenticated with valid credentials
    Returns True if valid, False otherwise
    """
    try:
        # Get token using async method
        token = await page.client_storage.get_async('access')
        if not token:
            print("No auth token found")
            return False

        # Use async request with timeout
        response = await async_build_request(page, TEST_URL)
        
        # Handle possible response errors
        if response.get('status') != 200:
            print(f"Auth check failed with status: {response.get('status')}")
            if 'error' in response:
                print(f"Error details: {response['error']}")
            return False

        print("Auth validated successfully")
        return True

    except Exception as e:
        print(f"Auth check error: {str(e)}")
        return False

def check_server_connection(timeout: float = 5.0) -> bool:
    """Check server availability with timeout"""
    try:
        requests.get(TEST_URL, timeout=timeout)
        print("Server is live...")
        return True
    except requests.exceptions.RequestException as e:
        print(f"Server connection failed: {str(e)}")
        return False

async def async_check_server_connection(timeout: float = 5.0) -> bool:
    """Check server availability (async version)"""
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(TEST_URL, timeout=timeout) as _:
                print("Server is live...")
                return True
    except aiohttp.ClientError as e:
        print(f"Server connection failed: {str(e)}")
        return False