# yaml test script to load and verify our configs
# todo arg parse
import yaml
from functools import reduce


class Config:
    def __init__(self, filename="config.yml"):
        self.filename = filename
        self.config = self.load_config()

    def load_config(self, filename=None):
        if not filename:
            filename = self.filename
        with open(filename) as f:
            config = yaml.load(f, Loader=yaml.SafeLoader)
            return config

    def get(self, key, config=None):
        if not config:
            config = self.config
        return reduce(lambda c, k: c[k], key.split('.'), config)


if __name__ == "__main__":
    cfg = Config()
    config = cfg.load_config("config.yml")
    print(config)
    print(config['input']['root_media'])
    print(cfg.get('input.root_media', config))
    print(cfg.get('input.root_media'))

