from flask import Flask
import time

app = Flask(__name__)

@app.route('/')
def hello():
    time.sleep(10)
    return "Hello world!"

if __name__ == '__main__':
    app.run(host='localhost', port=5000)