from flask import Flask

app = Flask(__name__)

@app.route('/')
def root():
    return """
    oh my god you saw me UwU
    """

@app.route('/calculator')
def calculator():
    return """
    <h1>Calculator</h1>
    <ul>
        <li><a href="/calculator/addition/1/1">Addition</a></li>
        <li><a href="/calculator/subtraction/1/1">Subtraction</a></li>
        <li><a href="/calculator/multiplication/1/1">Multiplication</a></li>
        <li><a href="/calculator/division/1/1">Division</a></li>
        <li><a href="/calculator/power/1/1">Power</a></li>
        <li><a href="/calculator/modulo/1/1">Modulus</a></li>
    </ul>
    """
@app.route('/calculator/addition/<int:a>/<int:b>')
def cal_add(a, b):
    answer = a + b
    text = f"{a} + {b} = {answer}"
    return text

@app.route('/calculator/subtraction/<int:a>/<int:b>')
def cal_sub(a, b):
    answer = a - b
    text = f"{a} - {b} = {answer}"
    return text

@app.route('/calculator/multiplication/<int:a>/<int:b>')
def cal_mul(a, b):
    answer = a * b
    text = f"{a} * {b} = {answer}"
    return text

@app.route('/calculator/division/<int:a>/<int:b>')
def cal_div(a, b):
    if b == 0:
        return "Cannot divide by zero"
    answer = a / b
    text = f"{a} / {b} = {answer}"
    return text

@app.route('/calculator/power/<int:a>/<int:b>')
def cal_pow(a, b):
    answer = a ** b
    text = f"{a} ** {b} = {answer}"
    return text

@app.route('/calculator/modulo/<int:a>/<int:b>')
def cal_mod(a, b):
    if b == 0:
        return "Cannot divide by zero"
    answer = a % b
    text = f"{a} % {b} = {answer}"
    return text

if __name__ == '__main__':
    app.run(debug=True)