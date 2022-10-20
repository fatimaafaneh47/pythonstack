
from unicodedata import name
from flask import Flask, render_template , request,session ,redirect

app = Flask(__name__)    
app.secret_key = 'keep it secret, keep it safe' 

@app.route('/')
def create():
    if 'name' in session:
        print('key exists!')
        
    else:
        print("key 'key_name' does NOT exist")
        session['name'] =0
       
   
    
    count = session['name']
    count+=1
    session['name']=count
    return render_template('index.html',t=session['name'])
   
@app.route('/destroy')
def dest():
    session['name'] =0
    return render_template('index.html')
    

if __name__=="__main__":   
    app.run(debug=True) 
    
