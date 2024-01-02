#!/usr/bin/env python3
'''
This module introduces a class.
'''
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''
    class that inherits from BaseCaching and is a caching system.
    '''
    def __init__(self):
        '''
        Initializing the class.
        '''
        super().__init__()

    def put(self, key, item):
        '''
        assigning the dictionary key value pairs.
        '''
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            first_key = next(iter(self.cache_data))
            del self.cache_data[first_key]
            print(f"DISCARD: {first_key}")

        self.cache_data[key] = item

    def get(self, key):
        '''
        Getting the key value pair
        '''
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
