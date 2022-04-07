from flask import Flask

app = Flask(__name__)

@app.route('/') # this is what is typed into the browser http://localhost:5000/ <- base route
def hello_world():
    print("this is showing a request on '/'")
    return "Hello World"


@app.route("/dojo")
def dojo():
    print("Dojo")
    return "Dojo!"


@app.route("/say/flask")
def flask():
    print("saying hi flask")
    return "Hi Flask!"


@app.route("/say/michael")
def michael():
    print("saying hi Michael")
    return "Hi Michael!"



@app.route("/say/john")
def john():
    print("saying hi John")
    return "Hi John!"




@app.route('/say/flask/<string:name>/<int:num>')
def number(name, num):
    print("saying numbers")
    return (f'Hi {name}' * num)











if __name__ == "__main__":
    app.run(debug = True)