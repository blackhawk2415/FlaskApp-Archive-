from flask import Flask, render_template, flash, request, url_for, redirect 
from content_management import content
from wtforms import Form, StringField




from dbconnect import connection 



TOPIC_DIC = content()


 
app = Flask(__name__)

@app.route('/')
def homepage():

    title = "Epic Tutorials"
    paragraph = ["wow I am learning so much great stuff!wow I am learning so much great stuff!wow I am learning so much great stuff!wow I am learning so much great stuff!","wow I am learning so much great stuff!wow I am learning so much great stuff!wow I am learning so much great stuff!wow I am learning so much great stuff!wow I am learning so much great stuff!wow I am learning so much great stuff!wow I am learning so much great stuff!wow I am learning so much great stuff!wow I am learning so much great stuff!"]

    try:
        return render_template("index.html", title = title, paragraph=paragraph, dashboard="/dashboard")
    except Exception, e:
        return str(e)

@app.route('/dashboard/')
def dashboard():
	flash("Flash test")
	return render_template("dashboard.html", TOPIC_DIC = TOPIC_DIC)


@app.route('/slashboard/')
def slashboard():
	try:
		return render_template("dashboard.html", TOPIC_DIC = Slashboard)
	except Exception as e:
		return render_template("500.html", error=e)



@app.route('/login/', methods = ['GET', 'POST'])
def login_page():
	error = None 	
	try:
		if request.method == "POST":
			attempted_username = request.form['Username']
			attempted_password = request.form['Password']

			flash(attempted_username)
			flash(attempted_password)


			if attempted_username == "admin" and attempted_password == "password":
				return redirect(url_for('dashboard'))

			else: 
				error = "Bad username or password, please try again."


		return render_template("login.html", error=e)

	except Exception as e:
		flash(e)
		return render_template("login.html", error=e)




@app.route("/register/", methods = ['GET', 'POST'])
def register_page():
	try:
		return("register page")
		c, conn = connection()
	except Exception as e:
		return(str(e))
	

class RegistrationForm(Form):
	username = StringField("Username", [validators.Length(min=4, max=20)])		
	


@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html") 

 
if __name__ == "__main__":
	app.run(debug = True, host='0.0.0.0', port=8080, passthrough_errors=True)
