# Set up your imports and your flask app.
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    # This home page should have the form.
    return render_template('home.html')


# This page will be the page after the form
@app.route('/report')
def report():
    # Check the user name for the 3 requirements.

    # HINTS:
    # https://stackoverflow.com/questions/22997072/how-to-check-if-lowercase-letters-exist/22997094
    # https://stackoverflow.com/questions/26515422/how-to-check-if-last-character-is-integer-in-raw-input

    # Return the information to the report page html.

    username = request.args.get('username')
    result = check_username(username)

    return f'<h1>{result}</h1>'


def check_username(username):
    if len(username) < 3:
        return False

    if not any(c.islower() for c in username):
        return False

    if not any(c.isupper() for c in username):
        return False

    if not username[-1].isdigit():
        return False

    return True


if __name__ == '__main__':
    # Fill this in!
    app.run(debug=True)
