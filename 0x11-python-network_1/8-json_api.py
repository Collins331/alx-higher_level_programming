#!/usr/bin/python3
""""import requests and sys"""
import requests as r
import sys as s

if __name__ == "__main__":
    """send a post request to url wth data parameter"""
    if len(s.argv) == 2:
        q = s.argv[1]
    else:
        q = ""
    res = r.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        res_dict = res.json()
        if res_dict:
            print("[{}] {}".format(res_dict.get('id'), res_dict.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
