import json


config_path = "config/config.json"

with open(config_path) as config_file:
    config_json = json.loads(config_file.read())

def get_config(key):
    return config_json[key]
