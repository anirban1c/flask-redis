#!/usr/bin/env python
import pytest
import requests
import json


def run():
    ## for X-Allow 
    r = requests.get(url="http://169.254.169.254/metadata/instance?api-version=2017-08-01&format=text",
            headers={'Metadata': 'true',
            })
    try:
        _j = json.loads(r.text)
    except Exception as ae:
        raise



if __name__ == '__main__':
    run()