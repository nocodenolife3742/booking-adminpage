from flask import Flask, render_template, request, jsonify
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
    search = request.args.get('search') or None
    id = request.args.get('id') or None
    data = Guest.query.all()
    if search:
        data = filter(lambda x: search in x.guest_name or
                                search in x.contact_email or
                                search in x.contact_phone, data)
    if id:
        data = filter(lambda x: id == str(x.guest_id), data)
    return render_template('customers.html', theme=theme, guests=data)


@app.route('/bookings')
def bookings():
    theme = request.args.get('theme') or 'light'
    search = request.args.get('search') or None
    data = Booking.query.all()
    if search:
        data = filter(lambda x: search in x.guest.guest_name or search in str(x.check_in_date) or search in str(
            x.check_out_date) or search in str(x.total_price), data)
    return render_template('bookings.html', theme=theme, bookings=data)


@app.route('/')
def main():
    theme = request.args.get('theme') or 'light'
    return render_template('main.html', theme=theme)


@app.route('/delete_booking', methods=['POST'])
def delete_booking():
    booking_id = request.json.get('booking_id')
    try:
        booking = Booking.query.get(booking_id)
        database.session.delete(booking)
        database.session.commit()
        return jsonify({'success': True})
    except:
        print('error')
        database.session.rollback()
        return jsonify({'success': False})


if __name__ == '__main__':
    app.run(debug=True)
