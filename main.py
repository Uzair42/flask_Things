from flask import Flask ,redirect ,url_for,render_template,request,session

app = Flask (__name__)

isLogin=True
list = [ "ali ",'khalil']
# Define a route for the home page
@app.route('/')
def dashborad():
    return render_template("index.html",list=list, title="Dashboard",name="ai_powered survillance")

# Redirecting to Student Analytics Page
@app.route('/student')
def Student():
    if isLogin==False:
        return redirect(url_for("dashborad"))
    else :
        return "Student Analytics Page"
    
# passing parameter in url 
@app.route('/student/<name>')
def Student_name(name):
        return f"Analytics of , {name}!"


@app.route('/teacher')
def teacher():
    return "Teacher's Page"


# Redirct with url parameter 
@app.route('/teacher/<name>')
def redirect_students(name):
     return redirect(url_for("Student_name",name=name))



# inherents the Child template in base template
@app.route("/base")
def base():
     return render_template("child.html")


# dictionary to store user and password
users = {
    'ali': '1234',
    'pak': 'pak'
}

@app.route('/login')
def Login():
     return render_template("login.html")
@app.route('/handle_get', methods=['GET'])
def handle_get():
    if request.method == 'GET':
        username = request.args['username']
        password = request.args['password']
        print(username, password)
        if username in users and users[username] == password:
            return '<h1>Welcome!!!</h1>'
        else:
            return '<h1>invalid credentials!</h1>'
    else:
        return render_template('login.html')



@app.route('/handle_post', methods=['POST'])
def handle_post():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(username, password)
        if username in users and users[username] == password:
            return '<h1>Welcome!!!</h1>'
        else:
            return '<h1>invalid credentials!</h1>'
    else:
        return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)

