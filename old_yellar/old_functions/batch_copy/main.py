'''BATCH COPY/LOAD PROCESS'''

import multiprocessing
import datetime as dt
import logging
import json
import re
import os

import boto3
from flask import current_app
from psycopg2.extras import LoggingConnection
import psycopg2


# LOAD CURRRENT APP CONFIGURATION
CONFIG = current_app.config


def handle(event, context):
    print("running batch copy")
    print(CONFIG)

if __name__ == '__main__':
    handle('a', 'b')
