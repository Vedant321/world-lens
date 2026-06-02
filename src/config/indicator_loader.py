import yaml


def load_indicators():
    with open("config/indicators.yml", "r") as file:
        config = yaml.safe_load(file)

    return config["indicators"]