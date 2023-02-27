from flask import Flask,render_template,url_for,request,redirect;
app=Flask(__name__)

@app.route('/')
def home():
    return "This is the Home!!!"

@app.route('/login', methods=['POST','GET'])
def Login():
    if request.method=='POST':
        user=request.form['nm']
        age=request.form['age']
        return redirect(url_for("User", usr=user, age=age))
    else:
        return render_template("login.html")


@app.route("/<usr>/<age>")
def User(usr,age):
    return f"<h3>{usr} and {age} </h3>"

@app.route('/merchant')
def Merchant():
    return render_template('Customer/merchant.html')

if __name__=='__main__':
    app.debug=True;
    app.run()



