#!/usr/bin/env python3
"""Task 0 Module"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """class BasicCache that inherits from BaseCaching
    and is a caching system
    """
    def put(self, key, item):
        """Adds an item to the caching system
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Gets a value from the caching system
        """
        return self.cache_data.get(key)
