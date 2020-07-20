import json
import requests
import numpy as np
import pandas as pd
from sklearn import datasets


"""Setting the headers to send and accept json responses
"""
header = {'Content-Type': 'application/json', \
                  'Accept': 'application/json'}

"""Reading test batch
"""
iris = datasets.load_iris()
X, y = iris.data, iris.target

df = pd.DataFrame(X[0:1])
print(type(df))

"""Converting Pandas Dataframe to json
"""
data = df.to_json(orient='records')
print(type(data))

"""POST <url>/predict
"""
resp = requests.post("http://0.0.0.0:8000/predict", \
                    data = json.dumps(data),\
                    headers= header)

print(resp.status_code)

"""The final response we get is as follows:
"""
print(resp.json())
