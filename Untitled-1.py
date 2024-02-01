
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data to store books
books = [
    {'id': 1, 'title': 'Book 1', 'author': 'Author 1', 'publication_year': 2020},
    {'id': 2, 'title': 'Book 2', 'author': 'Author 2', 'publication_year': 2021},
]

# Model for Book
class Book:
    def __init__(self, title, author, publication_year):
        self.id = len(books) + 1
        self.title = title
        self.author = author
        self.publication_year = publication_year

# Route to display the list of books
@app.route('/books')
def book_list():
    return render_template('books.html', books=books)

# Route to add a new book
@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        publication_year = int(request.form['publication_year'])

        new_book = Book(title, author, publication_year)
        books.append(new_book.__dict__)

        return redirect(url_for('book_list'))

    return render_template('add_book.html')

if __name__ == '__main__':
    app.run(debug=True)
