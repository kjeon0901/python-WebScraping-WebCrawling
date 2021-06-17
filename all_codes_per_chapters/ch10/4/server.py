from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hi():
    print(request.method)
    return 'Hello World!'

@app.route('/api1', methods=['GET'])
def test1():
    print(request.method)
    return 'test1'

@app.route('/api2', methods=['POST'])
def test2():
    print(request.method)
    return 'test2'

if __name__ == '__main__':
    app.run()
