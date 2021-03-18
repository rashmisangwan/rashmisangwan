from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about_handler():
  return '<h1> about </h1>'

@app.route('/contact')
def contact_handler():
  return '<h1> contact </h1>'


if __name__ == "__main__":
    app.run(debug=True)
