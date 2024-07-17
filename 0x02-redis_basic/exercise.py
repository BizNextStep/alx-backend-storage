#!/usr/bin/env python3
"""
Redis Cache module
"""

import redis
import uuid
from typing import Union, Callable, Optional

class Cache:
    """
    Cache class to interact with Redis and store data.
    """

    def __init__(self):
        """
        Initialize the Cache class with a Redis client and flush the database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis with a randomly generated key.

        Args:
            data (Union[str, bytes, int, float]): The data to be stored in Redis.

        Returns:
            str: The randomly generated key under which the data is stored.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float, None]:
        """
        Retrieve data from Redis by key and optionally apply a conversion function.

        Args:
            key (str): The key to look up in Redis.
            fn (Optional[Callable]): The function to convert the data.

        Returns:
            Union[str, bytes, int, float, None]: The retrieved data, optionally converted.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """
        Retrieve data from Redis and convert it to a string.

        Args:
            key (str): The key to look up in Redis.

        Returns:
            str: The retrieved data as a string.
        """
        return self.get(key, lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """
        Retrieve data from Redis and convert it to an integer.

        Args:
            key (str): The key to look up in Redis.

        Returns:
            int: The retrieved data as an integer.
        """
        return self.get(key, int)

    def increment(self, key: str, amount: int = 1) -> int:
        """
        Increment the value of a key by a specified amount.

        Args:
            key (str): The key to increment in Redis.
            amount (int, optional): The amount to increment by. Defaults to 1.

        Returns:
            int: The new value after incrementing.
        """
        return self._redis.incr(key, amount)

if __name__ == "__main__":
    cache = Cache()

    TEST_CASES = {
        b"foo": None,
        123: int,
        "bar": lambda d: d.decode("utf-8")
    }

    for value, fn in TEST_CASES.items():
        key = cache.store(value)
        assert cache.get(key, fn=fn) == value

    data = b"hello"
    key = cache.store(data)
    print(key)

    local_redis = redis.Redis()
    print(local_redis.get(key))

    # Testing increment
    increment_key = cache.store(10)
    print(cache.get_int(increment_key))
    cache.increment(increment_key, 5)
    print(cache.get_int(increment_key))

