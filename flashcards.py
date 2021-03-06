from flask import (Flask, render_template, request, abort,
                   jsonify, redirect, url_for)
from model import db, save_db

# Flask Constructor
app = Flask(__name__)

# Decorator - View Function
@app.route('/')
def index_view():
    return render_template('index.html',
                           cards=db,
                           pagetitle="Flask App")

@app.route('/card/<int:index>')
def card_view(index):
    try:
        card = db[index]
        max_index = len(db) - 1
        return render_template('card.html',
                               card = card,
                               index=index,
                               max_index=max_index,
                               pagetitle="Flash Card")
    except IndexError:
        abort(404)

@app.route('/add_card', methods=['POST', 'GET'])
def add_card_view():
    if request.method == 'POST':
        # form has been submitted, process data
        card = {"question": request.form['question'],
                 "answer": request.form['answer']}
        db.append(card)
        save_db()
        return redirect(url_for('card_view', index=len(db)-1))
    return render_template('add_card.html', pagetitle="Add Card")

#Remove card
@app.route('/remove_card/<int:index>', methods=['GET', 'POST'])
def remove_card_view(index):
    try:
        card = db[index]
        if request.method == 'POST':
            # del db[index]
            db.remove(card)
            save_db()
            return redirect(url_for('index_view'))
        return render_template('remove_card.html',
                               card=card,
                               index=index,
                               pagetitle="Remove Flash Card")
    except IndexError:
        abort(404)

# SERVING REST API
@app.route('/api/card')
def api_card_list():
    return jsonify(db)

@app.route('/api/card/<int:index>')
def api_card_detail(index):
    try:
        return jsonify(db[index])
    except IndexError:
        abort(404)



if __name__ == '__main__':
    app.run(debug=True)

#In command prompt type: export FLASK_APP=nameoftheapp.py
#In command prompt type: export FLASK_ENV=developemnt
#In windows OS command prompt type: set FLASK_APP=nameoftheapp.py
#In windows OS command prompt type: set FLASK_ENV=developemnt
