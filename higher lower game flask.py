from flask import Flask
import random

app = Flask(__name__)

# Generate the random number between 0 and 9
random_number = random.randint(0, 9)

@app.route('/')
def game():
    return '<h1>Guess A Number Between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'

# Dynamic route to handle the user's guess
@app.route('/<int:number_entered>')
def check(number_entered):
    # Too Low
    if number_entered < random_number:
        return '<h1 style="color: red">Sorry, Too Low!</h1>'  \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'

    # Too High
    elif number_entered > random_number:
        return '<h1 style="color: blue">Sorry, Too High!</h1>'  \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'

    # Correct Guess
    else:
        return '<h1 style="color: green">You Found Me!</h1>'     \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'

# Standard Way To Start Flask Server.
# app.run is placed within the if statement.
if __name__ == '__main__':
    app.run(debug=True)

