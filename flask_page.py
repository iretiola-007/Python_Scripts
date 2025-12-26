from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask world!"

if __name__ == "__main__":
    app.run(debug=True)

# running flask
# run "python app.py" on your terminal and visit the url

# this will start a local web server and show your message when you open the URL that shows up in your terminal (http://127.0.0.1:5000)

# note: replace "app.py" in the command: "python app.py" with your actual file name