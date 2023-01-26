import json
import argparse
# import yaml
import utils
import requests
import datetime
import argparse
import os
from tqdm import tqdm
import glob
from urllib import request
from dotenv import load_dotenv
load_dotenv()

output_dir = os.environ['output_dir'] + "/api/" + "media"

files = glob.glob(output_dir + "/*.json")

for file in tqdm(files):
    with open(file) as f:
        df = json.load(f)

    render = df["o:renderer"]

    if render == "iiif":
        url = df["o:source"].replace("/info.json", "/full/full/0/default.jpg")

    else:
        url = df["o:original_url"]

    
    path = os.environ['output_dir'] + "/files/oid/{}.jpg".format(df["o:id"])

    if os.path.exists(path):
        continue

    os.makedirs(os.path.dirname(path), exist_ok=True)


    request.urlretrieve(url, path)
