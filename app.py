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

@app.route('/hw3')
def hw3():
    return render_template('hw3.html')

@app.route('/hw4')
def hw4():
    return render_template('hw4.html')

@app.route('/hw5')
def hw5():
    return render_template('hw5.html')

@app.route('/hw6')
def hw6():
    return render_template('hw6.html')

@app.route('/hw7')
def hw7():
    return render_template('hw7.html')

@app.route('/hw8')
def hw8():
    return render_template('hw8.html')

@app.route('/hw9')
def hw9():
    return render_template('hw9.html')

@app.route('/hw10')
def hw10():
    return render_template('hw10.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True)
