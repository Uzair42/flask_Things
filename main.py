from flask import Flask ,redirect ,url_for,render_template

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



if __name__ == '__main__':
    app.run()

