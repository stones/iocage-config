import json

def load(filepath):
    with open(filepath , 'r') as stream:
        try:
            return json.load(stream)
        except json.JSONDecodeError as exc:
            print(exc)

