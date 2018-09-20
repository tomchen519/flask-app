from flask import current_app


def handle(event, context):
    print("running test")
    config = current_app.config
    print(config)


if __name__ == '__main__':
    handle('a', 'b')