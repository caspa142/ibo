from integration import *
from flask import Flask

app = Flask(__name__)


@app.route('/numericalintegralservice/<lower>/<upper>')
def index(lower, upper):
    result = ""
    for n in N:
        i = integral(fn, n, float(lower), float(upper))
        result += "<p> n=" + str(n) + ": " + str(i) + "</p>"
    return result


@app.route('/health')
def health():
    result = "I'm alive 😎\n"
    return result


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
