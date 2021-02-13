from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<name>')
def show_name(name):
    return f"Hi {name.title()}!"

@app.route('/repeat/<int:num>/<word>')
def repeat_word(num, word):
    return word * num

@app.route('/<error>')
def give_error(error):
    return "Sorry! No response. Try again."

if __name__=="__main__":
    app.run(debug=True)