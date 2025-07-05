from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    try:
        response = requests.get("https://catfact.ninja/fact", timeout=5)
        response.raise_for_status()
        data = response.json()
        fact = data.get('fact', "No fact found.")
    except Exception as e:
        print(f"Error fetching cat fact: {e}")
        fact = "Unable to load a cat fact at the moment. 🐾"
    return render_template("index.html", fact=fact)


if __name__ == '__main__':
    app.run()
