#!/usr/bin/env python3
'''
module introduces a class
'''
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    '''
    Class that inherits from the basecaching.
    '''

    def __init__(self):
        '''
        Initializing the class
        '''
        super().__init__()
        self.insertion_order = []

    def put(self, key, item):
        '''
        Assigning key value pairs
        '''
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key = self.insertion_order.pop()
            del self.cache_data[last_key]
            print(f"DISCARD: {last_key}")

        self.cache_data[key] = item
        self.insertion_order.append(key)

    def get(self, key):
        '''
        Method for getting item using the key
        '''
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
