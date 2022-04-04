import os
import sys
from dotenv import load_dotenv

load_dotenv()

test = os.getenv("TEST", 'not found test')


class Config:
    """
    General configuration parent class
    """
    TEST = test

class DevelopmentConfig(Config):
    """
    Development configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    """
    DEBUG = True

class ProductionConfig(Config):
    """
    Production configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    """
    DEBUG = False


app_config = dict(
    dev=DevelopmentConfig,
    prod=ProductionConfig
)

