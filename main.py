from flask import Flask, jsonify, render_template, request
from forms import FactorialForm
import os

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

def factit(num1):
    if (num1 == 1 or num1 == 0):
        return 1
    else:
        return (num1 * factit(num1 - 1))

@app.route('/', methods=['GET', 'POST'])
def add_numbers():
    num1 = None
    op = None
    form = FactorialForm()

    if request.method == 'POST':
        num1 = form.num1.data
        op = factit(num1)

    return render_template('factorial.html', form=form, sum=op)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')