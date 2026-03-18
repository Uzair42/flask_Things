from flask import  Flask , request, session, render_template,url_for


app=Flask(__name__)


userdb={
    'admin':'admin12',
    'ali' : "321"
}

@app.route('/')
def home():
    return "render_template('index.html')"

@app.route('/login',methods=["GET","POST"])
def login():
    if request.method=='POST':
        username=request.form['usernamePost']
        password=request.form['passwordPost']
        if username in userdb and userdb[username] == password:
            return "Welcome g {usename}" 
        else :
            return " Galat password "
    
    else :
        return render_template('login.html') 

        



if __name__ == '__main__':
    app.run(debug=True)