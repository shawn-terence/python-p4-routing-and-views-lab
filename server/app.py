#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:route>')
def print_string(route):
    print(route)
    return route
@app.route('/count/<int:num>')
def count(num):
        count = f''
        for n in range(num):
            count += f'{n}\n'
        return count
@app.route('/math/<int:num1>/<string:operator>/<int:num2>')
def math(num1,operator,num2):
    if operator =='-':
        return str(num1-num2)
    elif operator =='*':
        return str(num1*num2)
    elif operator=='+':
        return str(num1 + num2)
    elif operator == 'div':
        return str(num1 / num2)
    elif operator == '%':
        return str(num1 % num2)
    return 'error'
if __name__ == '__main__':
    app.run(port=5555, debug=True)
