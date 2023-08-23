#!/usr/bin/env python3
'''
FIFO (First In First Out) caching
'''


from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''
    FIFOCache class using FIFO caching and inherits from BaseCaching
    '''

    def __init__(self):
        '''
        Initializes the class
        '''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        '''
        Adds item to dictionary

        Args:
            key: Key value to reference dictionary
            item: Value to be inserted in dictionary

        Return: Dictionary updated
        '''
        if key is None or item is None:
            return

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {first_key}")

        self.cache_data[key] = item

    def get(self, key):
        '''
        Returns items from dictionary based on key

        Args:
            key: Key value to obtain value

        Return: Valued represented by key
        '''
        return self.cache_data.get(key, None)