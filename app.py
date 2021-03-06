from flask import Flask, jsonify, render_template
import json, os

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
@app.route("/maps")
def media():
    website_info = get_website_info()
    website_info['current'] = 'maps'
    return render_template("maps.html", info=website_info)

@app.route("/about")
def sources():
    website_info = get_website_info()
    website_info['current'] = 'About'
    return render_template("sources.html", info=website_info)
@app.errorhandler(404)
def page_not_found(error):
  return render_template('404.html'), 404

if __name__ == "__main__":
  #  var port = process.env.PORT || 7000
    app.run(host='0.0.0.0', port=7000)

