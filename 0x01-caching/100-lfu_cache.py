#!/usr/bin/env python3
"""Task 5 Module"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """class LFUCache that inherits from BaseCaching
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
            if key in self.cache_data:
                self.cache_data[key] = item
                self.keys.remove(key)
                self.keys.append(key)
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    del self.cache_data[self.keys[0]]
                    print("DISCARD: {}".format(self.keys[0]))
                    self.keys.pop(0)
                self.cache_data[key] = item
                self.keys.append(key)

    def get(self, key):
        """Gets a value from the caching system
        """
        if key in self.cache_data:
            self.keys.remove(key)
            self.keys.append(key)
        return self.cache_data.get(key)
