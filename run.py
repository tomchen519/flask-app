import os

from flaskr import create_app

config_name = os.getenv('APP_SETTING')
app = create_app(config_name)

if __name__ == '__main__':
    flaskr.run()