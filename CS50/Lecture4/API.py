# E:\Python>python -u "e:\Python\CS50\Lecture4\API.py" warfaze
import requests
import sys
import json

if len(sys.argv) < 2:
    sys.exit()

response = requests.get(
    "https://itunes.apple.com/search?entity=song&limit=5&term=" + sys.argv[1]
)
track = response.json()
for result in track["results"]:
    print(result["trackName"])
