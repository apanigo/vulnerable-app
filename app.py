from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('hello.html')

@app.route('/cat')
def cat():
    return render_template('cat.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

