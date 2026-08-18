# Book Alchemy

   A Flask web application for managing a digital library. Users can add authors and books, view the collection with book covers, search by title, sort by title or author, and delete books.

---

## Features

- Add authors (name, birth date, optional date of death)
- Add books (ISBN, title, publication year, author)
- Display all books with cover images from Open Library Covers API
- Sort books by title or author name
- Search books by title keyword
- Delete books; automatically removes authors who have no remaining books
- User-friendly success and error messages

---

## Technologies

- Python 3
- Flask
- Flask-SQLAlchemy
- SQLite
- Jinja2
- HTML

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Mr-Miller777/book-alchemy
   cd book_alchemy
   ```
   
2. (Optional) Create and activate a virtual environment:
   
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
   
3. Install dependencies:

   ```bash
   pip install flask sqlalchemy flask_sqlalchemy jinja2
   ```
   
4. Ensure the data/ directory exists (create it if missing):
   
   ```bash
   mkdir -p data
   ```
   - The SQLite database file library.sqlite will be created automatically when the application starts.

5. Run the Flask app:

   ```bash
   flask run --host=0.0.0.0 --port=5002
   ```

6. Open your browser and go to http://localhost:5002.

---

## Usage

| Route        | Method   | Description   |
|--------------|----------|---|
| /            | GET      |Home page – lists all books, supports search & sort|
| /add_author	 | GET/POST |Add a new author |
|/add_book|	GET/POST|	Add a new book (select author from dropdown)|
|/book/<int:book_id>/delete|	POST|	Delete a book; removes author if no books remain|

---

## Project Structure
   
```text
book_alchemy/
├── data/
│   └── library.sqlite      # SQLite database (auto-generated)
├── templates/
│   ├── add_author.html     # Form for adding authors
│   ├── add_book.html       # Form for adding books
│   └── home.html           # Home page displaying books
├── app.py                  # Flask application and routes
├── data_models.py          # SQLAlchemy models (Author, Book)
└── README.md
```

---

## License

   This project is for educational purposes as part of a coding assignment.

---
