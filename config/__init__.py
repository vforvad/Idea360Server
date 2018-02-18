import os

from .base import BaseConfig
from .development import DevelopmentConfig
from .test import TestConfig

app_config = {
    'development': DevelopmentConfig,
    'test': TestConfig
}
