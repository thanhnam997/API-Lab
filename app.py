from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Using instructor-provided API key
    api_key = "AIzaSyCdtcEmCii8bNySWzGtpwwWmwBDjp2nKi4"
    return render_template('index.html', api_key=api_key)

if __name__ == '__main__':
    app.run(debug=True)