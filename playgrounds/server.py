from turtle import color
from flask import Flask , render_template

app = Flask(__name__)  

@app.route('/play')          
def play():
     return render_template("index3.html",repeat=3,box_color="blue")

@app.route('/play/<x>')          
def level2(x):
    return render_template('index3.html', repeat=int(x),box_color="blue")

@app.route('/play/<x>/<color>')
def level3(x,color):
    return render_template("index3.html",repeat=int(x),box_color=color)

if __name__=="__main__":  
    app.run(debug=True)
