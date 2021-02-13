from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def showBoard():
    return render_template("index.html")

@app.route('/<number>')
def changeBoard(number):
    return render_template("index2.html", number=int(number))

@app.route('/<num1>/<num2>')
def lastChange(num1,num2):
    return render_template("index3.html", num1=int(num1), num2=int(num2))

if __name__=="__main__":
    app.run(debug=True)