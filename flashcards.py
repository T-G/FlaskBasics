from flask import Flask, render_template, abort, jsonify
from model import db

# Flask Constructor
app = Flask(__name__)

# Decorator - View Function
@app.route('/')
def welcome():
    return render_template('index.html',
                           cards=db,
                           pagetitle="Flask App")

@app.route('/card/<int:index>')
def card_view(index):
    try:
        card = db[index]
        return render_template('card.html',
                               card = card,
                               index=index,
                               pagetitle="Flash Card")
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
