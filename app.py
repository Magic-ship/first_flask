from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Welcome to my first flask app!"
    
@app.route("/educative")
def learn():
    return "I am happy to learning at educative!"

if __name__ == "__main__":
    app.run(debug = True, host = '0.0.0.0', port = 3000)
    