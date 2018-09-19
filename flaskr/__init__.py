import os
import importlib
import datetime as dt

from flask import Flask, request

from instance.config import app_config
# from apscheduler.schedulers.background import BackgroundScheduler
# from apscheduler.triggers.cron import CronTrigger

def create_app(config_name):
    # create and configure app
    print("create app")
    app = Flask(__name__, instance_relative_config=True)

    print(config_name)

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

        module = 'flaskr.functions.{}.main'.format(function_name)
        handle = 'handle'
        mod = importlib.import_module(module)
        func = getattr(mod, handle)
        result = func('a', 'b')

        print('function {} completed at {}\n'.format(function_name, dt.datetime.now()))

        # print(request.method)
        # print(request.get_json().get('account'))
        # print(request.get_json().get('set'))
        # print(request.get_json().get('brand'))

    @app.route('/old/<function_name>', methods=['GET', 'POST'])
    def run_old_func(function_name):
        print('old function: {}'.format(function_name))

        module = 'flaskr.old_functions.{}.main'.format(function_name)
        handle = 'handle'
        mod = importlib.import_module(module)
        func = getattr(mod, handle)
        result = func('a', 'b')

        return 'function completed'

    from . import db
    print("registering db")
    db.init_app(app)

    # with app.app_context():
    #     scheduler = BackgroundScheduler()
    #     scheduler.add_job(run_func('app_function_test'), CronTrigger.from_crontab('* * * * *'))

    #     scheduler.start()

    return app
