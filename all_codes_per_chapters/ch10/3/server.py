from flask import Flask

app = Flask(__name__)

@app.route('/')
def hi():
    return 'Hello World!'

@app.route('/api1')
def test1():
    return 'test1'

@app.route('/api2')
def test2():
    return 'test2'

if __name__ == '__main__':
    app.run()
