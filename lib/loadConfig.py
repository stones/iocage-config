import yaml

def load(filepath):
    with open(filepath , 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

