from flask import current_app
from .. import Utility as util

import datetime as dt
import json
import os


def handle(setting, context):
    print(setting)
    ENV = setting['environment']
    FUNCTION_NAME = setting['name']
    util.init_function(FUNCTION_NAME)
    config = current_app.config
    print(config)


if __name__ == '__main__':
    handle('a', 'b')