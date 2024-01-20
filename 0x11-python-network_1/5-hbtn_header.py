#!/usr/bin/python3
"""import requests and sys"""
import requests as r
import sys as s

if __name__ == "__main__":
    """request header details for url"""
    res = r.get(s.argv[1])
    print(res.headers['X-Request-Id'])
