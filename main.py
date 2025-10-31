from flask import Flask ,redirect ,url_for

app = Flask (__name__)

isLogin=True

# Define a route for the home page
@app.route('/')
def dashborad():
    return "Administration Dashboard"

@app.route('/student')
def Student():
    if isLogin==False:
        return redirect(url_for("dashborad"))
    else :
        return "Student Analytics Page"

@app.route('/student/<name>')
def Student_name(name):
    
    return f"Analytics of , {name}!"


if __name__ == '__main__':
    app.run()

