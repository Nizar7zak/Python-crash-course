import json
with open('questions.json', 'r') as f:
    data = json.load(f)

# print(data)

with open('questions.json', 'w') as f:
    json.dump(f)
