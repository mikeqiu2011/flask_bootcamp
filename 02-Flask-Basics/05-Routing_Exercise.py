# Set up your imports here!
# import ...
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/') # Fill this in!
def index():
    # Welcome Page
    # Create a generic welcome page.
    return render_template('home.html')

@app.route('/puppy') # Fill this in!
def puppylatin(name):
    # This function will take in the name passed
    # and then use "puppy-latin" to convert it!

    # HINT: Use indexing and concatenation of strings
    # For Example: "hello"+" world" --> "hello world"
    pass

if __name__ == '__main__':
    # Fill me in!
    app.run(debug=True)
