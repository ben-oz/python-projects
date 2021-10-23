from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

all_books = []


@app.route('/')
def home():
    return render_template('index.html', arg_books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        added_book = {
            "title": request.form['book_name'],
            "author": request.form['author_name'],
            "rating": request.form['book_rating']
        }
        all_books.append(added_book)
        return redirect(url_for('home'))  # it will redirect to home page after adding the new book

    return render_template('add.html')


if __name__ == "__main__":
    app.run(debug=True)

