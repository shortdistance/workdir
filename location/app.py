from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def sing_point():
    #return "nihao"
    return render_template('html5-googlemap.html')


@app.route("/muti")
def muti_point():
    return render_template('html5-googlemap-muti.html')

@app.route("/simple")
def simple():
    return render_template('simple.html')


if __name__ == '__main__':
    app.run('127.0.0.1', 5000, debug=True)