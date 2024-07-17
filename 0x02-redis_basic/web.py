#!/usr/bin/env python3
"""
Web Cache module
"""

import redis
import requests
from typing import Callable
from functools import wraps

r = redis.Redis()

def count_access(func: Callable) -> Callable:
    """
    Decorator to count the number of accesses to a URL.
    """
    @wraps(func)
    def wrapper(url: str) -> str:
        count_key = f"count:{url}"
        r.incr(count_key)
        return func(url)
    return wrapper

def cache_result(expiration: int) -> Callable:
    """
    Decorator to cache the result of a URL fetch with an expiration time.
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(url: str) -> str:
            cache_key = f"cache:{url}"
            cached_result = r.get(cache_key)
            if cached_result:
                return cached_result.decode('utf-8')
            result = func(url)
            r.setex(cache_key, expiration, result)
            return result
        return wrapper
    return decorator

@count_access
@cache_result(expiration=10)
def get_page(url: str) -> str:
    """
    Fetch the HTML content of a URL and cache the result.

    Args:
        url (str): The URL to fetch.

    Returns:
        str: The HTML content of the URL.
    """
    response = requests.get(url)
    return response.text

if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk"
    print(get_page(url))
    print(f"Access count: {r.get(f'count:{url}').decode('utf-8')}")
    print(get_page(url))  # This should fetch from cache
    print(f"Access count: {r.get(f'count:{url}').decode('utf-8')}")

