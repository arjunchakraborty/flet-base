from flet import *
import requests
import aiohttp
import asyncio


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