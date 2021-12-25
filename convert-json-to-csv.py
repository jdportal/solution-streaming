from pandas import json_normalize
import os
import json
path = '/var/log/logs/input-json'
for filename in os.listdir(path):
    a, b = os.path.splitext(os.path.join(path,filename))
    if b in '.json':
        with open(os.path.join(path,filename), 'r') as f:
            data = json.load(f)
        data_transformed = json_normalize(data)
        data_transformed.to_csv('/var/log/logs/output-csv/output-'+filename.replace("json", "csv"), index=None)
