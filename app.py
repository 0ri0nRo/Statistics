from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hw1')
def hw1():
    return render_template('hw1.html')

@app.route('/hw2')
def hw2():
    return render_template('hw2.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
