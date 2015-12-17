from flask import Flask, jsonify, render_template
import json

app = Flask(__name__)
app.config["DEBUG"] = True

#section title
#subheading
#paragraph stuff
website_info = None

@app.route("/")
def hello():
    website_info = get_website_info()
    website_info['current'] = 'hello'
    return render_template("hello.html", info=website_info)
def get_website_info():
    global website_info
    if not website_info:
        with open('data/website_info.json') as f:
            website_info = json.loads(f.read())
    return website_info

@app.route("/hello")
def home():
    website_info = get_website_info()
    website_info['current'] = 'hello'
    return render_template("hello.html", info=website_info)
@app.route("/maps")
def map():
    website_info = get_website_info()
    website_info['current'] = 'maps'
    return render_template("maps.html", info=website_info)

@app.route("/languages")
def lang():
    website_info = get_website_info()
    website_info['current'] = 'languages'
    return render_template("languages.html", info=website_info)

@app.route("/analysis")
def analysis():
    website_info = get_website_info()
    website_info['current'] = 'analysis'
    return render_template("analysis.html", info=website_info)
if __name__ == "__main__":
    app.run(host="0.0.0.0")

