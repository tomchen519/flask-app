from flask import current_app

config = current_app.config

print(config)

def handle(event, context):
    print("running old test")

if __name__ == '__main__':
    handle('a', 'b')