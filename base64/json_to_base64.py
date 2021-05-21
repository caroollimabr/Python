import json
import base64

dict_data = {"linguagem": "Python"}
json_data = json.dumps(dict_data)
print(json_data)
print(type(json_data))
json_b64 = base64.b64encode(json_data.encode('utf-8'))
print(json_b64)