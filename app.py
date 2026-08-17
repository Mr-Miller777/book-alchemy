import os
from flask import Flask, render_template, request
from datetime import datetime
from data_models import db, Author, Book

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'data/library.sqlite')}"

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/')
def home():
    sort = request.args.get('sort')
    if sort == 'title':
        books = Book.query.order_by(Book.title).all()
    elif sort == 'author':
        books = Book.query.join(Author).order_by(Author.name).all()
    else:
        books = Book.query.all()
    return render_template('home.html', books=books)


@app.route('/add_author', methods=['GET', 'POST'])
def add_author():
    if request.method == 'POST':
        name = request.form.get('name')
        birthdate_str = request.form.get('birthdate')
        date_of_death_str = request.form.get('date_of_death')

        birth_date = datetime.strptime(birthdate_str, '%Y-%m-%d').date() if birthdate_str else None
        date_of_death = datetime.strptime(date_of_death_str, '%Y-%m-%d').date() if date_of_death_str else None

        new_author = Author(name=name, birth_date=birth_date, date_of_death=date_of_death)
        db.session.add(new_author)
        db.session.commit()

        success_message = "Author added successfully!"
        return render_template('add_author.html', success_message=success_message)

    return render_template('add_author.html')


@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        isbn = request.form.get('isbn')
        title = request.form.get('title')
        publication_year = int(request.form.get('publication_year'))
        author_id = int(request.form.get('author_id'))

        new_book = Book(isbn=isbn, title=title, publication_year=publication_year, author_id=author_id)
        db.session.add(new_book)
        db.session.commit()

        success_message = "Book added successfully!"
        authors = Author.query.all()
        return render_template('add_book.html', authors=authors, success_message=success_message)

    authors = Author.query.all()
    return render_template('add_book.html', authors=authors)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)