from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
books = [
    {"id": 1, "title": "Atomic Habits", "author": "James Clear"},
    {"id": 2, "title": "Deep Work", "author": "Cal Newport"}, # HyperMedia Systems by Mike Amundsen
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/read')
def read():
    return render_template('read.html', books=books)

@app.route('/create', methods=['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('create.html')
    books.append({"id": len(books) + 1, "title": request.form['title'], "author": request.form['author']})
    return redirect(url_for('read'))

@app.route('/update/<int:book_id>', methods=['GET', 'POST'])
def update(book_id):
    book = next((b for b in books if b['id'] == book_id), None)
    if request.method == 'POST':
        book['title'] = request.form['title']
        book['author'] = request.form['author']
        return redirect(url_for('read'))
    return render_template('update.html', book=book)

@app.route('/delete/<int:book_id>', methods=['DELETE'])
def delete(book_id):
    global books
    books = [b for b in books if b['id'] != book_id]
    return render_template('read.html', books=books)

if __name__ == '__main__':
    app.run(debug=True)
