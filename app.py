from flask import Flask, render_template
import requests

app = Flask(__name__)  

@app.route('/')
def home():
    try:
        response = requests.get("https://catfact.ninja/fact", timeout=5) #Sends a GET request to the API. If the server doesn't respond within 5 seconds, it will raise a timeout error.
        response.raise_for_status() # If the response status is not OK (i.e., not 200), it will raise an exception.
        data = response.json()  # Converts the JSON response from the API into a Python dictionary.
        fact = data.get('fact', "No fact found.") #If the 'fact' key is missing, it sets fact = "No fact found."
    except Exception as e:
        print(f"Error fetching cat fact: {e}") 
        fact = "Unable to load a cat fact at the moment. 🐾"
    return render_template("index.html", fact=fact)


if __name__ == '__main__':
    app.run()
