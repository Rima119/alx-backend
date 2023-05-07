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
            if len(self.cache_data) == BaseCaching.MAX_ITEMS\
                    and key not in self.keys:
                del_key = self.keys.pop()
                del self.cache_data[del_key]
                print("DISCARD: {}".format(del_key))
            if key in self.keys:
                self.keys.remove(key)
            self.cache_data[key] = item
            self.keys.append(key)

    def get(self, key):
        """Gets a value from the caching system
        """
        if key in self.keys:
            self.keys.remove(key)
            self.keys.append(key)
        return self.cache_data.get(key)
