from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/customers')
def customers():
    theme = request.args.get('theme') or 'light'
    return render_template('customers.html', theme=theme)


@app.route('/bookings')
def bookings():
    theme = request.args.get('theme') or 'light'
    return render_template('bookings.html', theme=theme)


@app.route('/')
def main():
    theme = request.args.get('theme') or 'light'
    return render_template('main.html', theme=theme)


if __name__ == '__main__':
    app.run()
