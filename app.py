from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello1():
    return 'test'

@app.route('/endpoint')
def hello2():
    return 'hellp'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
