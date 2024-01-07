from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/hotel'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
database = SQLAlchemy(app)


class Guest(database.Model):
    __tablename__ = 'guest'
    guest_id = database.Column(database.Integer, primary_key=True)
    guest_name = database.Column(database.String(255), nullable=False)
    contact_email = database.Column(database.String(255), nullable=False)
    contact_phone = database.Column(database.String(255), nullable=False)


class Booking(database.Model):
    __tablename__ = 'booking'
    booking_id = database.Column(database.Integer, primary_key=True)
    guest_id = database.Column(database.Integer, database.ForeignKey('guest.guest_id'), nullable=False)
    check_in_date = database.Column(database.Date, nullable=False)
    check_out_date = database.Column(database.Date, nullable=False)
    total_price = database.Column(database.Float, nullable=False)

    guest = database.relationship('Guest', backref='bookings')


@app.route('/customers')
def customers():
    theme = request.args.get('theme') or 'light'
    search = request.args.get('search') or ''
    data = Guest.query.filter(Guest.guest_name.like(f'%{search}%')).all()
    return render_template('customers.html', theme=theme, guests=data)


@app.route('/bookings')
def bookings():
    theme = request.args.get('theme') or 'light'
    search = request.args.get('search') or ''
    data = filter(lambda x: search in x.guest.guest_name or
                            search in str(x.check_in_date) or
                            search in str(x.check_out_date) or
                            search in str(x.total_price), Booking.query.all())
    return render_template('bookings.html', theme=theme, bookings=data)


@app.route('/')
def main():
    theme = request.args.get('theme') or 'light'
    return render_template('main.html', theme=theme)


if __name__ == '__main__':
    app.run(debug=True)
