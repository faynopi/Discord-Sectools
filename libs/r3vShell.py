from json import load
from libs.cfg import get_config

# Load json file
jsonFile = load(open(get_config("r3vShellsFile"), "r"))


def nameSearch(keyword):
    tmp = []
    tmp.append("Name:                 Description:          OperatingSystems:")
    tmp.append("=============================================================")
    for item in jsonFile:
        # check if keyword in description of item add item to the tmp list
        if keyword.lower() in item["desc"].lower():
            len1 = 10 - len(item["name"])
            len2 = 20 - len(item["desc"])
            tmp.append(
                f'{item["name"]} {" " * len1} {item["desc"]} {" " * len2} {item["meta"]}')
    # return tmp list
    return tmp

def list():
    tmp = []
    tmp.append("Name:                 Description:          OperatingSystems:")
    tmp.append("=============================================================")
    # for loop for add each item in json file and append to tmp list
    for item in jsonFile:
        len1 = 10 - len(item["name"])
        len2 = 20 - len(item["desc"])
        tmp.append(
            f'{item["name"]} {" " * len1} {item["desc"]} {" " * len2} {item["meta"]}')
        return tmp
        

def osSearch(keyword):
    tmp = []
    tmp.append("Name:                 Description:          OperatingSystems:")
    tmp.append("=============================================================")
    OperatingSystems = ["windows", "mac", "linux"]
    # check if keyword is in OperatingSystems otherwise return False
    if keyword.lower() in OperatingSystems:
        for item in jsonFile:
            if keyword.lower() in item["meta"]:
                len1 = 10 - len(item["name"])
                len2 = 20 - len(item["desc"])
                tmp.append(
                    f'{item["name"]} {" " * len1} {item["desc"]} {" " * len2} {item["meta"]}')
    else:
        return False
    return tmp


def r3vIt(name, ip, port, shell):
    try:
        tmp = ""
        for item in jsonFile:
            if name.lower() == item["name"]:
                tmp = item["command"].replace("{ip}", ip).replace(
                    "{port}", port).replace("{shell}", shell)
                return tmp
    except Exception as e:
        print(e)
        return False
