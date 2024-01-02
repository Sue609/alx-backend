#!/usr/bin/env python3
'''
Module introduces a class
'''
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    '''Class that inherits from the basecaching class'''

    def __init__(self):
        '''Initializing the class'''
        super().__init__()
        self.access_order = []

    def put(self, key, item):
        '''updating the key value pairs'''
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            recent_key = self.access_order.pop()
            del self.cache_data[recent_key]
            print(f"DISCARD: {recent_key}")

        self.cache_data[key] = item
        if key in self.access_order:
            self.access_order.remove(key)
        self.access_order.append(key)

    def get(self, key):
        '''getting the items using the key'''
        if key is None or key not in self.cache_data:
            return None

        self.access_order.remove(key)
        self.access_order.append(key)

        return self.cache_data[key]
