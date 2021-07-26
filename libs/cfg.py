import json


config_path = "config/config.json"

# Open config file and load as json
with open(config_path) as config_file:
    config_json = json.loads(config_file.read())

# get value of the key
def get_config(key):
    return config_json[key]
