from flask import Flask, render_template, json, request
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def main():
    return render_template('index.html')

@app.route('/dashboard.html')
def dashboard():
    return render_template('dashboard.html')

@app.route('/table.html')
def table():
    return render_template('table.html')

@app.route('/user.html')
def user():
    return render_template('user.html')

@app.route('/compose.html')
def compose():
    return render_template('compose.html')


if __name__ == "__main__":
    app.run(debug=True)
 