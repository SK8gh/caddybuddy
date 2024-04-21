#!/usr/bin/python3

from caddybuddy import CaddyBuddy
import requests


if __name__ == '__main__':
    """
    Demonstrating the proof-of-concept by optimizing baskets, dispatching them amongst available market places
    """
    BASE_URL = 'http://localhost:5000'

    url = f'{BASE_URL}/get_all_inventories/'

    # Send a GET request to the endpoint
    response = requests.get(url).json()

    caddy_buddy = CaddyBuddy(inventories=response)

    # Setting basket to optimize with associated quantity
    basket = {
        'COFFEE': 3,
        'SOAP': 10,
        'WINE': 2,
        'WATER': 1,
        'BMW': 1
    }

    caddy_buddy._process_prices(basket)
