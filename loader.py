import yaml

#Load configuration settings for the application.
class Loader:
    settings = yaml.safe_load(open("config.yml","r"))