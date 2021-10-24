from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///my_library.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Creating Table
class Book(db.Model):
    __tablename__ = 'books'       # normally class name is the table name but we override it
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

db.create_all()


@app.route('/')
def home():
    all_books = db.session.query(Book).all()
    count = len(all_books)
    return render_template('index.html', arg_count=count, arg_books=all_books)
    # query.all returns a list of objects. iterate it in index.html


@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        added_book = Book(
            title = request.form['book_name'],
            author = request.form['author_name'],
            rating = request.form['book_rating']
        )
        db.session.add(added_book)
        db.session.commit()

        return redirect(url_for('home'))  # it will redirect to home page after adding the new book

    return render_template('add_book.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
