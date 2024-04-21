#!/usr/bin/python3
import pandas as pd

from configuration import INVENTORY
from flask import Flask, jsonify
import logging


"""
This file contains the CaddyBuddy code, computing the optimal way to split baskets amongst supermarkets
"""


class CaddyBuddy:
    def __init__(self, inventories):
        self.inventories = inventories

    def _process_prices(self, basket):
        """
        For each product in the basket, ranking its price in the inventories of
        """
        # Computing available products (from the basket) for each market
        inventories = {m: {p: d for p, d in self.inventories[m].items() if p in basket}
                       for m in self.inventories}

        # Separating prices and quantities
        prices, quantities = [{s: {product: details.get(key) for product, details in v.items()}
                               for s, v in inventories.items()}
                              for key in ['PRICE', 'QUANTITY']]

        # Creating dataframe objects storing the prices and quantities separately
        prices, quantities = [pd.DataFrame(data=data) for data in [prices, quantities]]

        # Filling N/A values in the quantity dataframe
        quantities = quantities.fillna(0).astype(int)

        for product, desired_quantity in basket.items():
            p_prices, p_quantities = [df.loc[product].sort_values() for df in [prices, quantities]]

            raise NotImplementedError
