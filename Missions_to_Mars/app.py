# import dependencies
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Flask
app = Flask(__name__)

# PyMongo 
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")


@app.route("/")
def home():
    mars_info = mongo.db.mars.find_one()
    return render_template("index.html", mars_data=mars_info)

#scrape
@app.route("/scrape")
def scrape():
    mars_data = scrape_mars.scrape()

    mongo.db.mars.update({}, mars_data, upsert=True)

    return redirect("/")

# run
if __name__ == "__main__":
    app.run(debug=True)