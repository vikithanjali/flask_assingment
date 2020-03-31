from flask import Flask,render_template,redirect,url_for,request,jsonify
from wtform_fields import *
from models.models import *

app = Flask(__name__)
app.secret_key = 'replace later'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:fission@localhost/db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route("/", methods=["GET","POST"])
def index():
    reg_form = RegistrationForm()
    if reg_form.validate_on_submit():
        username =reg_form.username.data
        password = reg_form.password.data
        salary = reg_form.salary.data
        id = reg_form.id.data

        user_object =Users.query.filter_by(username=username).first()
        if user_object:
            return jsonify("someone else has taken this username!")
        user=Users(username=username,password=password,salary=salary,id=id)
        db.session.add(user)
        db.session.commit()
        return jsonify("Inserted into DB!")

    return render_template("index.html",form=reg_form)
@app.route("/login", methods=["GET","POST"])
def login():

    error=None
    if request.method == "POST":
        user = Users.query.filter_by(username=request.form["username"]).first()
        if user:
            if request.form['username'] !=user.username or request.form['password'] !=user.password:
                error = 'Invalid credentials.Please try again.'
            else:
                return "login successful"
        else:
            return "Invalid credentials"

    return render_template("login.html",error=error)


# main driver function
if __name__ == '__main__':
    app.run(debug=True)

