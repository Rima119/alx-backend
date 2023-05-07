#!/usr/bin/env python3
"""Task 1 Module"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """class FIFOCache that inherits from BaseCaching
    and is a caching system
    """
    def __init__(self):
        """Initializes the class.
        """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """Adds an item to the caching system
        """
        if key and item:
            if key in self.keys:
                self.keys.remove(key)
            elif len(self.keys) >= self.MAX_ITEMS:
                del self.cache_data[self.keys[0]]
                print("DISCARD: {}".format(self.keys[0]))
                self.keys.pop(0)
            self.keys.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """Gets a value from the caching system
        """
        return self.cache_data.get(key)
