from flask import Flask, render_template
app = Flask(__name__)

books = [
    { 'id': 1, 'title': 'Clean Code', 'authors': 'Robert C. Martin' },
    { 'id': 2, 'title': 'The DevOps Handbook', 'authors': 'Gene Kim, Jez Humble, Patrick Debois, John Willis' },
    { 'id': 3, 'title': 'The Phoenix Project', 'authors': 'Gene Kim, Kevin Behr, George Spafford' },
    { 'id': 4, 'title': 'My Glorious Retribution', 'authors': 'Ryan Sharp' }
]

@app.route('/books')
def get_books():
    return render_template('book_list.html', books=books)

@app.route('/books/<id>')
def get_book(id):
  return render_template('book.html', book=books[int(id) - 1])
