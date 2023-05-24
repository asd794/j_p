import json
with open('config.json',mode='r',encoding='big5') as file:
    data = json.load(file)
print(data)
# print('name:',data['name'])
# print('version:',data['version'])