from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/hotel'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
database = SQLAlchemy(app)


@app.route('/customers')
def customers():
    theme = request.args.get('theme') or 'light'
    search = request.args.get('search') or ''
    print(search)
    data = [
        {'name': 'John Doe', 'email': '2h4gK@example.com', 'phone': '123-456-7890'},
        {'name': 'Keele', 'email': 'bonbonbomb@example.com', 'phone': '114-514-1919810'},
    ]
    return render_template('customers.html', theme=theme, guests=data)


@app.route('/bookings')
def bookings():
    theme = request.args.get('theme') or 'light'
    search = request.args.get('search') or ''
    print(search)
    data = [
        {'name': 'John Doe', 'room': '101', 'checkin': '2022-01-01', 'checkout': '2022-01-02'},
        {'name': 'Jane Doe', 'room': '102', 'checkin': '2022-01-03', 'checkout': '2022-01-04'},
    ]
    return render_template('bookings.html', theme=theme, bookings=data)


@app.route('/')
def main():
    theme = request.args.get('theme') or 'light'
    return render_template('main.html', theme=theme)


if __name__ == '__main__':
    app.run(debug=True)
