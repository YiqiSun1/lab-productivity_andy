import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--filepath')
args = parser.parse_args()

import json
from collections import Counter

lang_counter = Counter()

# this is equivalent to unzip -p
import zipfile
with zipfile.ZipFile(args.filepath, 'r') as zip_ref:
    for name in zip_ref.namelist():
        with zip_ref.open(name, 'r') as file:
            for i, line in enumerate(file):
                #print(line.decode('utf-8').strip())
                datum = json.loads(line)
                lang = datum['data']['lang']
                lang_counter[lang] += 1
                print('lang=', lang)
                print("lang_counter=", lang_counter)
                if i > 20:
                    break

with open('output', 'w') as fout:
    fout.write(json.dumps(lang_counter))

