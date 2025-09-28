
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

shopping_list = []

@app.route('/')
def index():
    return render_template('index.html', shopping_list=shopping_list)

@app.route('/add', methods=['POST'])
def add():
    item = request.form.get('item')
    if item:
        shopping_list.append(item)
    return redirect(url_for('index'))

@app.route('/delete/<int:item_index>')
def delete(item_index):
    if 0 <= item_index < len(shopping_list):
        shopping_list.pop(item_index)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
