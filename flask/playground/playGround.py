from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play')
def showBoxes():
    return render_template('index.html')

@app.route('/play/<times>')
def addBoxes(times):
    return render_template('index2.html',num_times=int(times))

@app.route('/play/<times>/<color>')
def changeColor(times, color):
    return render_template('index3.html',num_times=int(times),color=color)

if __name__=="__main__":
    app.run(debug=True)