from flask import Flask, render_template, flash, request, url_for, redirect, session
# session and g are used to track what the user is doing 
from content_management import content
from wtforms import Form, BooleanField, TextField, validators, PasswordField
from passlib.hash import sha256_crypt
from MySQLdb import escape_string as thwart
import gc


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
		form = RegistrationForm(request.form)
		
		if request.method == "POST" and form.validate():
			username = form.username.data
			email = form.email.data
			password = sha256_crypt.encrypt((str(form.password.data)))
			c, conn = connection()

			# Check if username exists
			x = c.execute("SELECT * FROM users WHERE username = (%s)", 
					(thwart(username)))
		
			if int(len(x)) > 0:
				flash("That username is already taken, please choose another")
				return render_template('register.html', form=form)

			else:
				c.execute("INSERT INTO users (username, password, email, tracking) VALUES (%s, %s, %s, %s)", (thwart(username), thwart(password), thwart(email), thwart("/home")))
				conn.commit()
				flash("Thanks for registering")
				c.close()
				conn.close()
				gc.collect()

				# session is essentially a dictionary and seen as cookie, that can store anything
				session['logged_in'] = True
				session['username'] = username

				return redirect(url_for('dashboard'))

		return render_template('register.html', form=form)

	except Exception as e:
		return(str(e))
	

class RegistrationForm(Form):
	username = TextField('Username', [validators.Length(min=4, max=25)])		
	email = TextField('Email Address', [validators.Length(min=6, max=50)])
	password = PasswordField('Password', [validators.Required(),
						validators.EqualTo('confirm', message="Pass Must Match")])
	confirm = PasswordField('Repeat Password')
	accept_tos = BooleanField('I accept TOS')	
	

@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html") 

 
if __name__ == "__main__":
	app.run(debug = True, host='0.0.0.0', port=8080, passthrough_errors=True)
