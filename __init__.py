from flask import Flask, render_template
from content_management import content

TOPIC_DIC = content()

 
app = Flask(__name__)

@app.route('/')
def homepage():

    title = "Epic Tutorials"
    paragraph = ["wow I am learning so much great stuff!wow I am learning so much great stuff!wow I am learning so much great stuff!wow I am learning so much great stuff!","wow I am learning so much great stuff!wow I am learning so much great stuff!wow I am learning so much great stuff!wow I am learning so much great stuff!wow I am learning so much great stuff!wow I am learning so much great stuff!wow I am learning so much great stuff!wow I am learning so much great stuff!wow I am learning so much great stuff!"]

    try:
        return render_template("index.html", title = title, paragraph=paragraph)
    except Exception, e:
        return str(e)

@app.route('/dashboard/')
def dashboard():
	return render_template("dashboard.html", TOPIC_DIC = TOPIC_DIC)



@app.erorhandler(404)
def page_not_found(e):
	return render_template("404.html") 

 
if __name__ == "__main__":
	app.run(debug = True, host='0.0.0.0', port=8080, passthrough_errors=True)
