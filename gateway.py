#!/usr/bin/python3

from configuration import INVENTORY
from flask import Flask, jsonify
import logging


"""
This file contains a 'create_service' function that will instantiate a Flask service emulating a supermarket public
    API. Using those simulated services, we'll demonstrate the POC computing the optimal baskets.
"""


def create_gateway():
    """
    Creating a service emulating the functioning of a gateway requesting different supermarket API services
    """
    app = Flask('Market gateway')

    @app.route('/get_inventory/<supermarket_name>', methods=['GET'])
    def get_inventory(supermarket_name):
        """
        Requesting the inventory of a supermarket
        """
        try:
            # The 'INVENTORY' dictionary acts as a public API service of the inputted supermarket
            return jsonify(INVENTORY[supermarket_name])
        except KeyError:
            # Specified supermarket has no available service yet
            return jsonify({'message': 'Unavailable supermarket'}), 404

    @app.route('/get_all_inventories/', methods=['GET'])
    def get_all_inventories():
        """
        Requesting all available inventories
        """
        # We'll store all available inventories in the following dictionary
        inventories = {}

        for market in INVENTORY:
            try:
                inventories[market] = get_inventory(market).json
            except Exception:
                msg = f"Could not retrieve inventory for specified market : {market}"
                logging.error(msg)

                return jsonify({'message': msg}), 404

        return jsonify(inventories)

    return app


if __name__ == '__main__':
    """
    Making the main gateway available for requests
    """
    service = create_gateway()

    try:
        logging.info(f"Running gateway emulated gateway service")
        service.run(debug=True)
    except Exception as e:
        logging.error(f"Could not run the gateway service")
        raise e
