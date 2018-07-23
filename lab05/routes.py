from server import app, valid_time
from flask import request, render_template
from Calculator import Calculator


@app.route('/', methods=['POST', 'GET'])
def interest_total():
    if request.method == 'POST':
        amount = float(request.form["amount"])
        rate = float(request.form["rate"])
        time = request.form["time"]
        if valid_time(time) == 0:
            total = "Enter a postive time!"
        else:
            a1 = Calculator(amount,rate)
            total = a1.total_interest(time)
            time = float(time)
        return render_template('interest_form.html',total = total)
    return render_template('interest_form.html', calc_total=True)


@app.route('/time', methods=['POST', 'GET'])
def time_interest():
    if request.method == 'POST':
        amount = float(request.form["amount"])
        rate = float(request.form["rate"])
        total = float(request.form["total"])
        a1 = Calculator(amount,rate)
        time = a1.total_interest(total)
        return render_template('time_form.html',time = time)
    return render_template('time_form.html', calc_time=True)


@app.route('/credits', methods=['GET'])
def credits():
    return render_template('credits.html', name = "Jian Tao, 2018s1")
