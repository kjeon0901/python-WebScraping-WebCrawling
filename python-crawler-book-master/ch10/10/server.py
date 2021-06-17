from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/<data>', methods=['GET'])
def hi(data):
    d = {
        'key1': data,
        'key2': data + '123'
    }
    return render_template('hello.html', name=d)

if __name__ == '__main__':
    app.run()
