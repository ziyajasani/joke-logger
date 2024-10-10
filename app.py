#!/usr/bin/python3

import json
import requests
import logging

url = "https://official-joke-api.appspot.com/random_joke"

response = requests.get(url)
response = json.loads(response.text)

id = response['id']
setup = response['setup']
punchline = response['punchline']

#print(id, setup, punchline)

#print(response.text)

logger = logging.getLogger(__name__)
logging.basicConfig(filename="joke.log", encoding="utf-8", level=logging.DEBUG)
logging.warning("%s:%s:%s", id, setup, punchline)
