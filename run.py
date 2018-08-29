import os
import sys

from flaskr import create_app

print(sys.argv)

config_name = os.getenv('APP_SETTING')
app = create_app(config_name)

if __name__ == '__main__':
    flaskr.run()