from flask import Flask, render_template


app = Flask(__name__)

@app.route('/') # this is what is typed into the browser http://localhost:5000/ <- base route
def table():

    users = [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'John', 'last_name' : 'Supsupin'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]


    print("this is showing a request on '/'")
    return render_template('index.html', users=users)










if __name__ == "__main__":
    app.run(debug = True)