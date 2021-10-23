from flask import Flask
import random

app = Flask(__name__)

random_number = random.randint(0, 9)


@app.route('/')
def home():
    return "<h1>" + "Guess a number between 0 and 9" + "</h1>" + \
           "<p>Put your number at the end of URL</p>" + \
           "<img src='https://media.giphy.com/media/mMkjWN1ziPio0/giphy.gif' width=400>"


@app.route('/<int:number>')
def choice(number):
    if number < random_number:
        result = "<h1 style='color:red;'>" + "Too low, try again!" + "</h1>" + \
                 "<p>Put your number at the end of URL</p>" + \
                 "<img src='https://media.giphy.com/media/PR3585ZZSvcHO9pa76/giphy.gif' width=400>"
    elif number > random_number:
        result = "<h1 style='color:red;'>" + "Too high, try again!" + "</h1>" + \
                 "<p>Put your number at the end of URL</p>" + \
                 "<img src='https://media.giphy.com/media/g8tLOZ6RWlDvRf5Kfp/giphy.gif' width=400>"
    else:
        result = "<h1 style='color:green;'>" + "You got it!" + "</h1>" + \
                 "<img src='https://media.giphy.com/media/l1IXZfq5v52dZoIbS/giphy.gif' width=400>"
    return result


if __name__ == '__main__':
    app.run(debug=True)
