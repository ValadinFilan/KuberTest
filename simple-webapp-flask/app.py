import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome!"

@app.route('/health')
def health():
    return 'OK'

@app.route('/ready')
def ready():
    return 'OK'

if __name__ == "__main__":
    sleep(10)
    app.run(host="0.0.0.0", port=8080)
