from configparser import ConfigParser


def read_config_data(file_path, section, key):
    config = ConfigParser()
    config.read(file_path)
    return config.get(section, key)

