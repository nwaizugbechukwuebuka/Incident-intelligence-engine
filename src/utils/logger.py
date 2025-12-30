import logging
import yaml

def setup_logging():
    with open("config/logging.yaml") as f:
        config = yaml.safe_load(f)
    logging.basicConfig(level=config['root']['level'], format=config['formatters']['default']['format'])

def log_event(event: str, data: dict = None):
    logging.info(f"{event}: {data}")
