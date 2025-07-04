import requests
from flask import Flask, render_template

app = Flask(__name__) #name variable hold current module

def get_cat_fact():
    url = "https://catfact.ninja/fact"
    
    response = requests.get(url)
    if response.status_code ==200:
        return response.json().get("fact","no fact found.")
    return "failed to get a cat fact"

@app.route("/", methods = ["GET"])
def index():
    fact = get_cat_fact()
    return render_template("index.html", cat_fact = fact)

if __name__ =="__main__":
    app.run(debug=True)