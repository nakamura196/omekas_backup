import json
import argparse
# import yaml
import utils
import requests
import datetime
import argparse
import os

from dotenv import load_dotenv
load_dotenv()

parser = argparse.ArgumentParser()

parser.add_argument("type", help='items, item_sets, ..')
parser.add_argument("--isInitOutputDir", help='flag to initialize output directory', default=False)
parser.add_argument("--start", help='page that starts from', default=1)

args = parser.parse_args()

target = args.type

isInitOutputDir = args.isInitOutputDir == "True"

'''
f = open("../settings.yml", "r+")
settings = yaml.safe_load(f)

output_dir = settings["output_dir"] + "/api/" + target
'''

output_dir = os.environ['output_dir'] + "/api/" + target

if isInitOutputDir:
    utils.initDir(output_dir)

api_url = os.environ['api_url'] # settings["api_url"]

settings = os.environ

# key_identity = os.environ['key_identity']
# key_credential = os.environ['key_credential']

# print(key_credential)

loop_flg = True
page = int(args.start)

query = ""
if "key_identity" in settings and settings["key_identity"] != None:
    query += "&key_identity=" + settings["key_identity"] + "&key_credential=" + settings["key_credential"]

while loop_flg:

    url = api_url + "/"+target+"?page=" + str(
        page) + query
    print(datetime.datetime.now(), url)

    page += 1

    data = requests.get(url).json()
    
    if len(data) > 0 and "errors" not in data:
        for i in range(len(data)):
            obj = data[i]

            oid = str(obj["o:id"])

            with open(output_dir+"/"+oid+".json", 'w') as outfile:
                json.dump(obj, outfile, ensure_ascii=False,
                            indent=4, sort_keys=True, separators=(',', ': '))

    else:
        loop_flg = False
