from flask import Flask, request

app = Flask(__name__)

@app.route('/test/<data>', methods=['GET'])
def hi(data):
    return data

@app.route('/api1', methods=['GET'])
def test1():
    return request.args.get('data')

@app.route('/api2', methods=['POST'])
def test2():
    return request.form['data']

if __name__ == '__main__':
    app.run()
