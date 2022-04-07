from flask import Flask, render_template, request, session, redirect


app = Flask(__name__)

app.secret_key = "bu dum dum da counter game"

@app.route('/')
def index():
    if 'counter' in session:
        session['counter'] +=1
    else:
        session['counter'] = 1


    return render_template('index.html')


@app.route('/count_reset')
def count_reset():
    session.clear()
    return redirect('/')

@app.route('/count_up_2')
def count_up_2():
    session['counter'] += 1
    return redirect('/')

@app.route('/count_by', methods=['POST'])
def count_by():
    session['counter'] += int(request.form['countby']) - 1
    return redirect('/')










if __name__ == "__main__":
    app.run(debug = True)