#We need to write code that will query the meta data of an instance within AWS or Azure or GCP and provide a json formatted output.

import requests

headers = {"Metadata": "true"}
response = requests.get("http://169.254.169.254/metadata/instance?api-version=2021-01-01", headers=headers)

metadata = response.json()
print(metadata)
