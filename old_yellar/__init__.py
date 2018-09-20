import datetime as dt
import importlib
import json
import os

from flask import Flask, request

from instance.config import app_config
# from apscheduler.schedulers.background import BackgroundScheduler
# from apscheduler.triggers.cron import CronTrigger

def create_app(config_name):
    # create and configure app
    print("create app")
    print(os.getcwd())
    app = Flask(__name__, instance_relative_config=True)

    with open('old_yellar/functions/function_config.json', 'r') as f:
        CONFIG = json.load(f)

    print(config_name)

    return_msg = 'function {} completed at {}\n'

    if config_name == 'production':
        load_dotenv(dotenv_path='../.prod.env')

    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('../instance/config.py')

    @app.route('/', methods=['GET', 'POST'])
    def home():
        return 'index page of app'

    @app.route('/run/<function_name>', methods=['GET', 'POST'])
    def run_func(function_name):
        print('running: {}'.format(function_name))
        function_config = CONFIG[function_name]
        module = 'old_yellar.functions.{}.main'.format(function_name)
        handle = 'handle'
        mod = importlib.import_module(module)
        func = getattr(mod, handle)
        result = func(function_config, 'b')

        print(return_msg.format(function_name, dt.datetime.now()))
        return return_msg.format(function_name, dt.datetime.now())

        # print(request.method)
        # print(request.get_json().get('account'))
        # print(request.get_json().get('set'))
        # print(request.get_json().get('brand'))

    @app.route('/old/<function_name>', methods=['GET', 'POST'])
    def run_old_func(function_name):
        print('old function: {}'.format(function_name))

        module = 'old_yellar.old_functions.{}.main'.format(function_name)
        handle = 'handle'
        mod = importlib.import_module(module)
        func = getattr(mod, handle)
        result = func('a', 'b')
        print(return_msg.format(function_name, dt.datetime.now()))
        return return_msg.format(function_name, dt.datetime.now())

    from . import db
    print("registering db")
    db.init_app(app)

    # with app.app_context():
    #     scheduler = BackgroundScheduler()
    #     scheduler.add_job(run_func('app_function_test'), CronTrigger.from_crontab('* * * * *'))

    #     scheduler.start()

    return app
