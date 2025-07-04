from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get("https://catfact.ninja/fact")
    data = response.json()
    fact = data['fact']
    return render_template("index.html", fact=fact)

if __name__ == '__main__':
    app.run()
