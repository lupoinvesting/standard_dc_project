import json
from pydantic import BaseModel, field_validator
from typing import Literal
from logging import DEBUG, INFO, WARNING, ERROR, CRITICAL

CONFIG_PATH = "config.json"  # change with default env variable from docker
LOG_LEVELS = {
    "DEBUG": DEBUG,
    "INFO": INFO,
    "WARNING": WARNING,
    "ERROR": ERROR,
    "CRITICAL": CRITICAL,
}


class GeneralValidator(BaseModel):
    # log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
    log_level: Literal[DEBUG, INFO, WARNING, ERROR, CRITICAL]
    log_path: str

    @field_validator("log_level", mode="before")
    @classmethod
    def transform(cls, value: str) -> int:
        try:
            return LOG_LEVELS[value]
        except KeyError:
            raise ValueError(
                f"Invalid log level: {value}. Must be one of {', '.join(LOG_LEVELS.keys())}"
            )


class Configuration(BaseModel):
    general: GeneralValidator


# Load the JSON data from the file into a dictionary
with open(CONFIG_PATH, "r") as file:
    config_dict = json.load(file)

# Parse the dictionary into a Configuration object
config = Configuration(**config_dict)
