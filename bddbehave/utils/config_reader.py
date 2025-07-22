import configparser
import os


class ConfigReader:
    config = configparser.ConfigParser()
    config_path = os.path.join(os.path.dirname(__file__), '../config/config.ini')
    config.read(config_path)

    @classmethod
    def get(cls, section, key):
        return cls.config.get(section, key)
