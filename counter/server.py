from flask import Flask, render_template , request,redirect,session
app = Flask(__name__)
app.secret_key = 'keep it secret,keep it safe'
@app.route('/')
def index():
    return render_template("index.html")

@app.route("/process",methods=['POST'])
def process_form():
    print("*"*50)
    print(request.form)
    print(f"adding user{request.form['username']}to the database")
    session['username']=request.form['username']
    session['usermail']=request.form['email']
    print(f"username submitted:{request.form['username']}")
    print(f"email submitted:{request.form['email']}")
    return redirect("/show")
    
@app.route("/show")
def show_results():
    return render_template("info.html")

if __name__=="__main__":
    app.run(debug=True)
