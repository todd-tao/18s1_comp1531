from flask import Flask

def valid_time(time):
    if isinstance(time, str):
        return 0
    elif time > 0:
        return 1
    else:
        return 0

app = Flask(__name__)
