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
    website_info['current'] = 'home'
    return render_template("hello.html", info=website_info)
def get_website_info():
    global website_info
    if not website_info:
        with open('data/website_info.json') as f:
            website_info = json.loads(f.read())
    return website_info

@app.route("/home")
def home():
    website_info = get_website_info()
    website_info['current'] = 'home'
    return render_template("hello.html", info=website_info)
@app.route("/media")
def media():
    website_info = get_website_info()
    website_info['current'] = 'media'
    return render_template("media.html", info=website_info)
@app.route("/maps")
def map():
    website_info = get_website_info()
    website_info['current'] = 'maps'
    return render_template("maps.html", info=website_info)

@app.route("/languages")
def languages():
    website_info = get_website_info()
    website_info['current'] = 'languages'
    return render_template("language.html", info=website_info)

@app.route("/celebrities")
def celebs():
    website_info = get_website_info()
    website_info['current'] = 'celebrities'
    return render_template("celebrities.html", info=website_info)
@app.route("/sources")
def sources():
    website_info = get_website_info()
    website_info['current'] = 'sources'
    return render_template("sources.html", info=website_info)
@app.errorhandler(404)
def page_not_found(error):
  return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0")

