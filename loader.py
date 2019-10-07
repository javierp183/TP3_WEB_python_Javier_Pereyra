import yaml

class Loader:
    settings = yaml.safe_load(open("config.yml","r"))