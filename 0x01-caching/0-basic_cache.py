#!/usr/bin/env python3
'''
This module introduces a class
'''
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''
    A class that inherits from BaseCaching and is a caching system.
    '''
    def __init__(self):
        '''
        Initializing the class.
        '''
        super().__init__()

    def put(self, key, item):
        '''
        method that assigns the dict key value pairs.
        '''
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        '''
        Returns the value in the self.cache_data linked to key
        '''
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
