from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_programmer():
    return '<h1>I am a Programmer, I have no life. This is my first Flask Application.</h1>'

if __name__ == "__main__":
    app.run(debug=True)