#!/usr/bin/python3

CARREFOUR_INVENTORY = {
    'BANANA': {
        'QUANTITY': 3,
        'PRICE': 0.15
    },
    'COFFEE': {
        'QUANTITY': 1,
        'PRICE': 8.75
    },
    'DIET_COKE': {
        'QUANTITY': 3,
        'PRICE': 1.25
    },
    'SOAP': {
        'QUANTITY': 4,
        'PRICE': 3.3
    },
    'WATER': {
        'QUANTITY': 4,
        'PRICE': 0.8
    },
    'WINE': {
        'QUANTITY': 2,
        'PRICE': 9.45
    }
}

FRANPRIX_INVENTORY = {
    'BANANA': {
        'QUANTITY': 5,
        'PRICE': 0.11
    },
    'COFFEE': {
        'QUANTITY': 0,
        'PRICE': 9.7
    },
    'DIET_COKE': {
        'QUANTITY': 2,
        'PRICE': 1.1
    },
    'SOAP': {
        'QUANTITY': 8,
        'PRICE': 3.5
    },
    'WATER': {
        'QUANTITY': 4,
        'PRICE': 0.85
    },
    'KETCHUP': {
        'QUANTITY': 2,
        'PRICE': 2.45
    }
}

LIDL_INVENTORY = {
    'BANANA': {
        'QUANTITY': 5,
        'PRICE': 0.11
    },
    'COFFEE': {
        'QUANTITY': 0,
        'PRICE': 9.7
    },
    'DIET_COKE': {
        'QUANTITY': 2,
        'PRICE': 1.1
    },
    'WATER': {
        'QUANTITY': 4,
        'PRICE': 0.85
    },
    'KETCHUP': {
        'QUANTITY': 2,
        'PRICE': 2.45
    },
    'WINE': {
        'QUANTITY': 4,
        'PRICE': 11.7
    }
}


"""
Inventory is stored as follows:
supermarket_name : {
    product 1: {available quantity: q, price: p} ,
    ... ,
    product n: ...
}
"""
INVENTORY = {
    'CARREFOUR': CARREFOUR_INVENTORY,
    'FRANPRIX': FRANPRIX_INVENTORY,
    'LIDL': LIDL_INVENTORY,
}
