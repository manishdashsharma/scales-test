from datacube import *
import json

response = json.loads(datacube_data_retrieval(
    api_key,
    "voc",
    "voc_user_management",
    {
        "workspace_owner_name": "VOCABC",
    },
    100000000,
    0,
    False
))

print(response)