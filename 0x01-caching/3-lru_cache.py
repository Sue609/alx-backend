#!/usr/bin/env python3
'''
This module introduces a class.
'''
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    '''
    Class that inherits from another class.
    '''

    def __init__(self):
        '''
        Initializig the class.
        '''
        super().__init__()
        self.queue = []

    def put(self, key, item):
        '''
        Adding a new item in the cache
        '''
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.queue.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru_key = self.queue.pop(0)
            del self.cache_data[lru_key]
            print(f"DISCARD: {lru_key}")

        self.cache_data[key] = item
        self.queue.append(key)

    def get(self, key):
        '''
        Getting the item by key.
        '''
        if key is None or key not in self.cache_data:
            return None
        self.queue.remove(key)
        self.queue.append(key)
        return self.cache_data[key]
