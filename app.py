from flask import Flask
from flask import render_template
#from views import general

app = Flask(__name__)



@app.route("/")
def index():
    return render_template('index.html')





@app.route("/monkey/<whomonkey>")
def monkey(whomonkey=None):
    result = "who's a monkey? " + whomonkey
    return render_template('monkey.html', monkey=result)





if __name__ == "__main__":
    app.debug = True
    app.run()

