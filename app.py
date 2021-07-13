from flask import Flask
app = Flask(__name__)

@app.rote("/")
def hello():
    return "olá mundo!!!"

if __name__ == "__main__":
    app.run()