#!/usr/bin/env python3
"""Task 4 Module
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """class MRUCache that inherits from BaseCaching
    and is a caching system
    """
    def __init__(self):
        """Initializes the MRUCache class.
        """
        super().__init__()
        self.mru = []

    def put(self, key, item):
        """Adds an item to the caching system
        """
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                print("DISCARD: {}".format(self.mru[-1]))
                del self.cache_data[self.mru[-1]]
                self.mru.pop()
            self.cache_data[key] = item
            self.mru.insert(0, key)

    def get(self, key):
        """Gets a value from the caching system
        """
        if key in self.cache_data:
            self.mru.remove(key)
            self.mru.insert(0, key)
        return self.cache_data.get(key)
